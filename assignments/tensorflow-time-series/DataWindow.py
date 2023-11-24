class DataWindow(object):
  def __init__(self, input_width, label_width, shift, dataset_dict, 
                label_columns=None, column_to_train=None):
    
    self.train_df = dataset_dict["train_scale_df"]
    self.val_df = dataset_dict["val_scale_df"]
    self.test_df = dataset_dict["test_scale_df"]

    # column that we want to predict
    self.label_columns = label_columns
    if label_columns is not None:
      self.label_columns_indices = {
        name: i for i, name in enumerate(label_columns)}
    
    self.column_to_train = column_to_train
    self.column_indices = {name: i for i, name in enumerate(self.column_to_train)}

    self.input_width = input_width
    self.label_width = label_width
    self.shift = shift

    self.total_window_size = input_width + shift

    self.input_slice = slice(0, input_width)
    self.input_indices = np.arange(self.total_window_size)[self.input_slice]

    self.label_start = self.total_window_size - self.label_width  # This is equal to self.input_width 
    self.label_slice = slice(self.label_start, None)   # from label_start to the end
                                                       # of self.total_window_size
    self.label_indices = np.arange(self.total_window_size)[self.label_slice]


  def split_to_inputs_labels(self, features):
    inputs = features[:, self.input_slice, :]
    labels = features[:, self.label_slice, :]
    if self.label_columns is not None:
      labels = tf.stack(
        [labels[:, :, self.column_indices[name]] for name in self.label_columns],
        axis=-1)

    inputs.set_shape([None, self.input_width, None])
    labels.set_shape([None, self.label_width, None])

    return inputs, labels


  def plot(self, model=None, plot_col="traffic_volume", max_subplots=3, 
            figsize=(12, 8), xlabel="Time"):
    inputs, labels = self.sample_batch

    fig, axes = plt.subplots(nrows=max_subplots, ncols=1, figsize=figsize, 
                              sharex=True)
    plot_col_index = self.column_indices[plot_col]
    max_n = min(max_subplots, len(inputs))

    for n in range(max_n):
      axes[n].plot(self.input_indices, inputs[n, :, plot_col_index],
                      label="Inputs", marker=".", zorder=-10)

      if self.label_columns:
        label_col_index = self.label_columns_indices.get(plot_col, None)
      else:
        label_col_index = plot_col_index

      if label_col_index is None:
        continue

      axes[n].scatter(self.label_indices, labels[n, :, label_col_index],
                          edgecolors="k", marker="s", label="Labels",
                          c="green", s=64)
      
      if model is not None:
        predictions = model(inputs)
        axes[n].scatter(self.label_indices, predictions[n, :, label_col_index],
                            marker="X", edgecolor="k", )
          
      
      y_label = "\n".join(textwrap.wrap(f"{plot_col} [scaled]", width=20))
      axes[n].set_ylabel(y_label)
      axes[n].grid("on")
    
    axes[-1].set_xlabel(xlabel)

    plt.show(fig)
      
  def __repr__(self):
    return "\n".join([
      f"Total window size: {self.total_window_size}", 
      f"Input indices: {self.input_indices}",
      f"Label indices: {self.label_indices}",
      f"Label column name(s): {self.label_columns}" 
    ])

  def make_dataset(self, data):
    # print(f"self.column_to_train: {self.column_to_train}")
    data = data[self.column_to_train]
    # print(f"data: {data}")
    data = np.array(data, dtype=np.float32)
    ds = tf.keras.preprocessing.timeseries_dataset_from_array(
      data=data, targets=None, sequence_length=self.total_window_size, 
      sequence_stride=1, shuffle=True, batch_size=32)
    
    ds = ds.map(self.split_to_inputs_labels)
    return ds

  def __repr__(self):
    return "\n".join([
      f"Total window size: {self.total_window_size}", 
      f"Input indices: {self.input_indices}",
      f"Label indices: {self.label_indices}",
      f"Label column name(s): {self.label_columns}" 
    ])
  
  @property
  def train(self):
    return self.make_dataset(self.train_df)

  @property
  def val(self):
    return self.make_dataset(self.val_df)

  @property 
  def test(self):
    return self.make_dataset(self.test_df)

  @property
  def sample_batch(self):
    result = getattr(self, '_sample_batch', None)
    if result is None:
      result = next(iter(self.train))
      self._sample_batch = result
    return result