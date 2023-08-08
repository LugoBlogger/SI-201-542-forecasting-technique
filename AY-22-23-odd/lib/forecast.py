import numpy as np
import pandas as pd
import scipy.stats as sc_stats
import tabulate

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

class Forecast(object):
  def __init__(self):
    return None

  def read_ods(filename, columns=None):
    if columns is None:
      df = pd.read_excel(filename, engine="odf", header=0)
    elif isinstance(column, list):
      df = pd.read_excel(filename, engine="odf", header=0, usecols=columns)
    else:
      key_arr = {k for k in columns.keys()}
      df = pd.read_excel(filename, engine="odf", header=0, usecols=key_arr)
      df = pd.rename(columns=columns)
    return df


  def std_error(r_k_arr, k, n):
    """A function to compute standard error of autocorrelation"""
    r_k_arr = np.array(r_k_arr)
    r_k_arr = r_k_arr[:k-1] if len(r_k_arr) > 1 else [0]
    r_k_arr = np.array(r_k_arr)
    return np.sqrt((1 + 2*sum(r_k_arr**2))/n)


  def get_correlogram(dataframe, up_to_lag, columns=[None, None], 
                    significance_lvl=0.05):
    """A function to calculate r_k, t_test, and LBQ"""
    df = dataframe.copy()

    Y_t = df[columns[1]].to_numpy()

    mean_Y_t = np.mean(Y_t)

    r_lag_arr = np.empty(up_to_lag)
    denom = np.sum((Y_t - mean_Y_t)**2)

    num_of_samples = len(Y_t)
    dof = num_of_samples - 1   # degree of freedom
    l_bound = sc_stats.t.ppf(significance_lvl/2, dof)
    u_bound = sc_stats.t.ppf(1-significance_lvl/2, dof)
    #print(f"[l_bound, r_bound] = [{l_bound}, {u_bound}]")

    std_error_arr = np.empty(up_to_lag)
    significance_lim_arr = np.empty([up_to_lag, 2])

    t_test_arr = np.empty(up_to_lag)

    # Ljung-Box Q statistic
    coeff = num_of_samples*(num_of_samples + 2)
    LBQ_arr = np.empty(up_to_lag)

    for lag in range(1, up_to_lag+1):
      numer = (Y_t[:-lag]  - mean_Y_t) * (Y_t[lag:] - mean_Y_t)
      numer = np.sum(numer)
      # print(f"numer = {numer}")
      # print(f"denom = {denom}")
      r_lag = numer / denom
      r_lag_arr[lag-1] = r_lag 
      std_error_arr[lag-1] \
        = Forecast.std_error(r_lag_arr[:lag], lag, num_of_samples)
      #print(f"std_error_r_{lag:<2d}: {std_error_arr[lag-1]}")
      significance_lim_arr[lag-1, 0] = l_bound*std_error_arr[lag-1]
      significance_lim_arr[lag-1, 1] = u_bound*std_error_arr[lag-1]

      t_test_arr[lag-1] = r_lag / std_error_arr[lag-1]
      # print(f"r_{lag:<2d} = {r_lag_arr[lag-1]:9.6f}")

      LBQ_arr[lag-1] = coeff*np.sum(
        (r_lag_arr[:lag]**2)/(num_of_samples - np.arange(1, lag+1)))


    df_result = pd.DataFrame({
      "k": np.arange(1, up_to_lag+1), 
      "r_k": r_lag_arr, 
      "t_test": t_test_arr, 
      "LBQ": LBQ_arr,
      "l_bound": significance_lim_arr[:,0],
      "u_bound": significance_lim_arr[:,1]  
    })
    return df_result


  def plot_autocorr_func(df_acorr_analysis, title=None):
    fig, ax = plt.subplots(figsize=(7, 3))

    lag_arr = df_acorr_analysis["k"].to_numpy()
    stem_handler = ax.stem(lag_arr, df_acorr_analysis["r_k"].to_numpy())

    ax.plot(lag_arr, df_acorr_analysis["l_bound"], 
      linestyle='--', color="gray")
    ax.plot(lag_arr, df_acorr_analysis["u_bound"], 
      linestyle='--', color="gray")

    # [0] = markerline handler
    # [1] = stemlines handler
    # [2] = baseline handler
    stem_handler[0].set_marker(None)
    stem_handler[1].set_linewidth(4)
    stem_handler[2].set_alpha(0)

    ax.grid("on")
    ax.set_ylim([-1.1, 1.1])
    ax.set_xlabel("Lag")
    ax.set_ylabel("Autocorrelation")
    ax.set_title(f"Autocorrelation Function for {title}\n"
      + "(with 5% significance limits for the autocorrelations)")

    plt.show(fig)



  def get_multiple_regress_coeff(df, n_vars=2, with_intercept=True):  

    regress_obj = LinearRegression(fit_intercept=with_intercept)

    if isinstance(df, pd.DataFrame):
      num_of_samples = len(df)
      X_arr = np.zeros((num_of_samples, n_vars))
      Y = df["Y"].to_numpy()

      for i in range(n_vars):
        key = f"X_{i+1}"
        X_arr[:, i] = df[key].to_numpy()

      regress = regress_obj.fit(X_arr, Y)
      df["hat_Y"] = regress.intercept_ + X_arr.dot(regress.coef_) 
    
    elif isinstance(df, np.ndarray):
      Y = df[:, 0]
      X_arr = df[:, 1:]

      
      regress = regress_obj.fit(X_arr, Y)
      Y_hat = regress.intercept_ + X_arr.dot(regress.coef_)
      df = np.column_stack([df, Y_hat])

    return regress, df


  def add_prediction_table(regress, x_regress_arr, df, n_vars, 
                            cofactor_matrix, significance_lvl=0.05):
    n_data = len(df)

    b0 = regress.intercept_
    b_arr = regress.coef_

    hat_Y = b0
    for i in range(n_vars):
      hat_Y += b_arr[i]*df[f"X_{i+1}"]

    
    data = [[]]
    fit = []
    prediction_interval = []
    for i, x_regress in enumerate(x_regress_arr):
      # display(cofactor_matrix) 
      X0_vector = np.ones(n_vars + 1)
      X0_vector[1:] = x_regress

      sumOfSquareY_of_hat_Y = ((df["Y"] - hat_Y)**2).sum()
      std_yx = np.sqrt(sumOfSquareY_of_hat_Y/(n_data - n_vars - 1))

      # -- for confidence interval (CI) and minitab S.E. of fit
      #    This measure the dispersion of the sample regression line
      #    about the population regression line
      #    The formula for multiple regression follow (Desalvo, 1971)
      std_err_fit = std_yx * np.sqrt(
        X0_vector.transpose().dot(cofactor_matrix).dot(X0_vector))
      std_forecast = std_yx * np.sqrt(
        1 + X0_vector.transpose().dot(cofactor_matrix).dot(X0_vector))
      # print(f"std_forecast: {std_forecast}")

      # -- 95% CI and 95% PI are computed using t-statistic although
      #    n_data > 30
      deg_of_freedom = n_data - n_vars - 1
      l_bound = sc_stats.t.ppf(significance_lvl/2, deg_of_freedom)
      u_bound = sc_stats.t.ppf(1 - significance_lvl/2, deg_of_freedom)


      Y_t = b0
      for j in range(n_vars):
        Y_t += b_arr[j]*x_regress[j]

      fit.append(Y_t)
      prediction_interval.append(
        [Y_t + l_bound * std_forecast, Y_t + u_bound * std_forecast])
      data.append([
        i+1, Y_t, std_err_fit, 
        f"({Y_t + l_bound * std_err_fit:.3f}, " \
           + f"{Y_t + u_bound * std_err_fit:.3f})",
        f"({Y_t + l_bound * std_forecast:.3f}, " \
           + f"{Y_t + u_bound * std_forecast:.3f})"])

    table_prediction = tabulate.tabulate(data, tablefmt='html', 
      headers=["New Obs", "Fit", "SE Fit", "95% CI", "95% PI"],
      floatfmt=[int, ".3f", ".3f", str, str])

    print(f"Predicted Values for New Observations")
    display(table_prediction)

    return fit, prediction_interval


  def add_predictor_table(x_regress_arr, new_column):
    data = [[]]
    for i, x_regress in enumerate(x_regress_arr):
      data.append([i+1, *x_regress])


    table_predictor = tabulate.tabulate(data, tablefmt="html",
      headers=["New Obs", *new_column[1:]], 
      floatfmt=[int, ".1f", int, int, int])

    print(f"Values of Predictors for New Observations")
    display(table_predictor)


  def get_minitab_out(df, n_vars=2, new_column=None, withCorrMatrix=False, 
                      withVIF=False, with_intercept=True, with_DW_stat=True, 
                      is_reg_diff=False, new_observ=0, x_regress=None):
    """
    new_column (dict) : a dictionary mapping to rename df header
    is_reg_diff:
      True - if we perform regression difference of Y_t and X_t. 
      In this function, it only implements how to print the output not the
      calculation
    new_observ: int
      Number of forecasting point.
    """
    
    data_struct = np.zeros((len(df), 1+n_vars))
    data_struct[:, 0] = df['Y']
    for i in range(n_vars):
      key = f"X_{i+1}"
      data_struct[:, i+1] = df[key]

    # -- compute correlation matrix
    corr_matrix = np.corrcoef(data_struct, rowvar=False)
    corr_matrix = corr_matrix[1:, 0:-1]    # only show lower triangle part 
                                           # of correlation matrix

    # -- compute regression intercept and coefficients
    regress, _ = Forecast.get_multiple_regress_coeff(df, n_vars=n_vars, 
                                            with_intercept=with_intercept)
    b_arr = [regress.intercept_] + regress.coef_.tolist()
    is_positive_b_arr = [b_j > 0 for b_j in b_arr]
    #print(f"b_arr: {b_arr}")
    
    # -- compute standad error of the estimates
    num_of_samples = len(df)
    hat_Y =  regress.intercept_ + data_struct[:,1:].dot(regress.coef_)
    sumSq_Y_hat_Y = ((data_struct[:, 0] - hat_Y)**2).sum()

    if with_intercept:
      s_yxs = np.sqrt(sumSq_Y_hat_Y/(num_of_samples - n_vars - 1))
    else:
      s_yxs = np.sqrt(sumSq_Y_hat_Y/(num_of_samples - n_vars))

    # -- compute cofactor matrix 
    if with_intercept:
      X_arr = np.ones_like(data_struct)
      X_arr[:,1:] = data_struct[:,1:]
    else:
      X_arr = data_struct[:, 1:]

    # this matrix is closely related to covariance matrix 
    cofactor_matrix = np.linalg.inv(X_arr.transpose().dot(X_arr))   
    

    # -- compute standard error of intercept_ and coef_
    # -- compute t-score of intecept_ and coef_
    # -- compute p-values of intercept_ and coef_
    SE_coef = np.zeros(1+n_vars)
    t_scores = np.zeros(1+n_vars)
    p_values = np.zeros(1+n_vars)
    
    if with_intercept:
      dof = num_of_samples - n_vars - 1;          # degrees of freedom
      for i in range(1+n_vars):
        SE_coef[i] = s_yxs*np.sqrt(cofactor_matrix[i, i])
        t_scores[i] = b_arr[i] / SE_coef[i]

        # .t.sf is a survival function (1 - cdf)
        p_values[i] = sc_stats.t.sf(abs(t_scores[i]), dof) * 2   
    else:
      dof = num_of_samples - n_vars;          # degrees of freedom
      for i in range(1, 1+n_vars):
        SE_coef[i] = s_yxs*np.sqrt(cofactor_matrix[i-1, i-1])
        t_scores[i] = b_arr[i] / SE_coef[i]

        # .t.sf is a survival function (1 - cdf)
        p_values[i] = sc_stats.t.sf(abs(t_scores[i]), dof) * 2   

    # -- compute VIF of coef_
    if withVIF:
      # if n_vars == 2, we calculate VIF from correlation matrix
      VIF_arr = np.zeros(n_vars)
      if n_vars == 2:
        VIF_arr[0] = 1/(1-corr_matrix[1, 1]**2)
        VIF_arr[1] = 1/(1-corr_matrix[1, 1]**2)
      else:
        for i in range(n_vars):
          # take a predictor column and put the other predictor after it
          predictor_data_struct = np.zeros((num_of_samples, n_vars))
          predictor_data_struct[:,0] = data_struct[:, i+1]   
          predictor_data_struct[:,1:] \
            = np.delete(data_struct, i+1, axis=1)[:,1:]  
          #print(predictor_data_struct)
          predictor_SST, predictor_SSR, _ \
            = get_sumSq(predictor_data_struct, n_vars=n_vars)
          predictor_R_sq = predictor_SSR/predictor_SST
          #print(predictor_R_sq)
          VIF_arr[i] = 1/(1 - predictor_R_sq)


    # -- compute ANOVA table
    meanY = data_struct[:, 0].mean()
    if with_intercept:
      SSR = ((hat_Y - meanY)**2).sum()
      SST = ((data_struct[:, 0] - meanY)**2).sum()
    else:
      SSR = (hat_Y**2).sum()
      SST = (data_struct[:, 0]**2).sum()

    SSE = ((data_struct[:, 0] - hat_Y)**2).sum()
    anova_sumSq = np.array([SSR, SSE, SST])

    if with_intercept:
      anova_dof = np.array([n_vars, num_of_samples - n_vars - 1, 
                            num_of_samples - 1], dtype=int)
    else:
      anova_dof = np.array([n_vars, num_of_samples - n_vars, 
                            num_of_samples], dtype=int)
    
    anova_meanSq = (anova_sumSq/anova_dof)[:2]
    anova_F_score = anova_meanSq[0] / anova_meanSq[1]

    # sf is a surfifal function (1 - cdf)
    anova_p_value = sc_stats.f.sf(anova_F_score, anova_dof[0], anova_dof[1])   

    # -- compute R_sq (coefficient of determination)
    R_sq = SSR/SST

    # -- compute adjusted R_sq
    adj_R_sq = 1 - (1 - R_sq)*(num_of_samples-1)/(num_of_samples-n_vars-1)
    
    # -- calculate Durbin-Watson statistics
    e_t = data_struct[:, 0] - hat_Y
    numerator = ((e_t[1:] - e_t[:-1])**2).sum()
    dw_stats = numerator / (e_t**2).sum()

    # -- create tabular form for correlation 
    if withCorrMatrix:
      data = []
      for i in range(n_vars):
        data_row = [new_column[i+1]] + \
          [f"{corr:.3f}" if j < i+1 else "" 
            for j, corr in enumerate(corr_matrix[i,:])]
        #print(data_row)
        #print([type(data_row_i) for data_row_i in data_row])
        data.append(data_row)

      table_corr = tabulate.tabulate(data, tablefmt='html', 
        headers=[""] + new_column[:n_vars], 
        floatfmt=["None"] + [".3f"]*(n_vars))

      print(f"Correlations: {', '.join(new_column)}")
      display(table_corr)

    # -- create tabular form for predictor
    data = [["Constant", b_arr[0], SE_coef[0], t_scores[0], p_values[0]]]
    if withVIF:
      for i in range(1, n_vars+1):
        data_row = [
          new_column[i], b_arr[i], SE_coef[i], t_scores[i], 
          p_values[i], VIF_arr[i-1]]
        data.append(data_row)
      table_predictor = tabulate.tabulate(data, tablefmt='html', 
        headers=["Predictor", "Coef", "SE Coef", "t-score", "p-value", "VIF"], 
        floatfmt=[None, ".4f", ".4f", ".2f", ".4f", ".3f"])
    else:
      for i in range(1, n_vars+1):
        data_row = [
          new_column[i], b_arr[i], SE_coef[i], t_scores[i], p_values[i]]
        data.append(data_row)
      table_predictor = tabulate.tabulate(data, tablefmt='html', 
        headers=["Predictor", "Coef", "SE Coef", "t-score", "p-value"], 
        floatfmt=[None, ".4f", ".4f", ".2f", ".4f"])


    print(f"Regression Analysis: {new_column[0]} versus "\
      + f"{', '.join(new_column[1:])}")
    print("The regression equation is")
    str_b_predictor = "" 
    for i in range(n_vars):
      sign = "+" if is_positive_b_arr[i+1] else "-"
      str_b_predictor += f" {sign} {abs(b_arr[i+1]):.3f} {new_column[i+1]}"
    if with_intercept:
      print(f"{new_column[0]} = {b_arr[0]:.3f}{str_b_predictor}")
    else:
      if str_b_predictor[1] == "+":
        str_b_predictor = str_b_predictor[3:]
      print(f"{new_column[0]} = {str_b_predictor}")
    display(table_predictor)
    if is_reg_diff:
      print(f"s_yxs = {s_yxs:.4f}")
    else:
      print(f"s_yxs = {s_yxs:.4f}   R_sq = {R_sq*100:.1f}%   "\
        + f"R-sq(adj) = {adj_R_sq*100:.1f}%")

    # -- create ANOVA table (with F-score and its p-value)
    data = [
      ["Regression",     anova_dof[0], anova_sumSq[0], 
        f"{anova_meanSq[0]:.4f}", f"{anova_F_score:.3f}", 
          f"{anova_p_value:.4f}"],
      ["Residual error", anova_dof[1], anova_sumSq[1], 
        f"{anova_meanSq[1]:.4f}", "", ""],
      ["Total",          anova_dof[2], anova_sumSq[2], "", "", ""]] 
    table_anova = tabulate.tabulate(data, tablefmt='html', 
      headers=["Source", "d.o.f", "sumSq", "meanSq", "F-score", "p-value"], 
      floatfmt=[None, ".0f", ".4f", "s", "s", "s"])

    print(f"Analyis of Variance")
    display(table_anova)

    # -- print Durbin-Watson statistics
    if with_DW_stat:
      print(f"Durbin-Watson Statistics = {dw_stats:.2f}")

    # -- make a prediction table
    fit = None
    prediction_interval = None
    if new_observ > 0:
      fit, prediction_interval \
        = Forecast.add_prediction_table(regress, x_regress, df, n_vars, 
                                        cofactor_matrix)

    # -- make predictor value for new observation
    if n_vars > 1 and new_observ > 0:
      Forecast.add_predictor_table(x_regress, new_column)
    


    return {"regress": regress, "param_stderr": SE_coef, 
      "param_t_stat": t_scores, "param_p_vals": p_values,
      "corr_matrix": corr_matrix, "R_sq": R_sq, "dw_stats": dw_stats, 
      "fit": fit, "prediction_interval": prediction_interval}
