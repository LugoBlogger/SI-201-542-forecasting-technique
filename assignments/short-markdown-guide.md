The following is the short tutorial how to use markdown.  
It is better to show markdown preview in VSCode.

For the complete tutorial, visit: [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

Each section, subsection, and subsubsection are recommended to write using
header `#`.

# Section 1

## Subsection 1.1

### Subsubsection 1.1.1

### Subsubsection 1.1.2

## Subsection 1.2

# Section 2

# Section 3

# Text formatting

- Two separate between paragraphs, you can use one empty newline

  paragraph 1
  
  paragraph 2

- To make a newline, add two spaces at the end of sentences.

  line 1  
  line 2

  or using HTML linebreak `<br>`  
  line 1<br>line 2

- Text emphasize: **bold**, _italic_

- Inline monospace text (for code): `arima_model_best`

- Code block:
  ```py
  def rolling_forecast(df: Union[pd.Series, list], ...):
    # do some forecasting
  ```

# Add figures

Using markdown format (the figure with is maximized to the width of 
the image)
![Figure example](../figures/pexels-photo-41126.jpeg)

For the specific image width use HTML format  
<img src="../figures/pexels-photo-41126.jpeg" width=200>

Sometimes, figure location is outside the markdown file. You can
use `../` to move out the folder where markdown file is.

Do not use absolute path in image source path, please use relative path
to make your markdown code portable.

# Add tables

Using markdown format
| Col 1  | Col 2  |
|--------|--------|
| item a | item 1 |
| item b | item 2 |
| item c | item 3 |

Using HTML format
<table>
  <tr>
    <td> <b>Col 1
    <td> <b>Col 2
  <tr>
    <td> item a
    <td> item 1
  <tr>
    <td> item b
    <td> item 2
  <tr>
    <td> item c
    <td> item 3
</table>


# Add equations
For the complete tutorial, visit [KaTeX](https://katex.org/docs/supported)

- Inline equation `$ $`:   
  We use $\text{ARMA}(p,q)$ model in our forecasting

- Centered equation `$$ $$`:
  $$
    y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \epsilon_t
  $$
