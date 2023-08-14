# Jupyter Notebook for SI 201 542 (Forecasting Technique)

In the previous academic year, we used (Hanke, 2014) as the main reference
for this lecture.   

Now we shift to use more recent reference that uses Python as its main 
programming language and also explored some deep learning architecture. 

The following jupyter notebook files and all the data set 
in this repo is completely based on (Peixeiro, 2022). 
The notebooks of this book 
can be found in [Peixeiro's GitHub](https://github.com/marcopeix/TimeSeriesForecastingInPython)

## Tutorial to set Git in your computer
This tutorial is intended for Windows users. 
I didn't provide it for Linux users since the majority of students use 
Windows as their operating system.

### Installing Git application
- First, install the Git application for Windows from 
  [git-scm.com](https://git-scm.com/download/win). 
  Choose the "Standalone Installer" - 64-bit (as 32-bit laptops are now very rare, 
  select based on your architecture). 
  Follow the provided instructions or refer to 
  [this step-by-step tutorial](https://phoenixnap.com/kb/how-to-install-git-windows) 
  on phonenixap.com.

- Once you have the Git application installed on your computer, 
  open VSCode and create a new terminal by clicking on the menu 
  "Terminal > New Terminal." 
  A new terminal will appear in the lower window of VSCode. 
  Then, type the following:
  ```bash
  git --version
  ```
  It should display the version of your Git application. 
  If it doesn't, you should review your installation steps.

### SSH connection

To establish automatic connectivity between your GitHub account and your computer (or VSCode), you need to set up an SSH key on your computer. This tutorial follows the guidelines provided in the GitHub documentation for 
[generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) 
and
[adding it to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). 
We're assuming that you haven't created an SSH key before. If you already have one, we recommend generating a new one for consistency.

- Open Git Bash and input the following configuration. 
  Make sure to replace the email address with your GitHub email address:
  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```

- When prompted by Git Bash with the following question: 
  ```
  > Enter a file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):
  ```
  type in the path mentioned within the parentheses and replace "id" with any identifier you can easily recognize:
  ```
  > Enter a file in which to save the key (/c/Users/LENOVO/.ssh/id_ed25519): /c/Users/LENOVO/.ssh/github_ed25519
  ```

- Enter a passphrase when prompted by Git Bash. Remember this passphrase; 
  if you forget it, you'll need to recreate and reset the SSH key from the beginning.

- Add your SSH key to the ssh-agent by entering the following two commands 
  in Git Bash (replace "id" with the identifier you used in the previous step; 
  in our example, our identifier is "github"): 
  ```bash
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519
  ```

- Copy the SSH public key to the clipboard by entering the following command 
  in Git Bash (replace "id" with the identifier you used in the previous step; 
  in our example, our identifier is "github"):
  ```bash
  clip < ~/.ssh/id_ed25519.pub
  ```

- Navigate to "Settings" in your GitHub account (you can access the "Settings" 
  menu by clicking your profile photo). 
  In the sidebar, go to the "Access" section and click on SSH and GPG keys.

- Click on "New SSH key" or "Add SSH Key." Provide a meaningful title in 
  the "Title" field for the new key. 
  For instance, if you're using a personal laptop, you could name this key 
  "Personal Laptop."

- In the "Key" field, paste your public key (use Ctrl + V to paste since 
  you've already copied it to your clipboard). Then, click on "Add SSH key."

- You can now utilize commands such as "git clone" and "git pull" 
  to copy and retrieve repositories from GitHub. 
  
- If you encounter an error like this:
  ```
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  ```
  Enter the following command in Git Bash: `ssh-keygen -R github.com`

## References
- (Peixiero, 2022) Time Series with Python
- (Hanke, 2014) - Business Forecasting
- (Anderson, 1976) - Time series analysis and forecasting - The Box-Jenkins Approach
- (Bartlett, 1946) - On the theoretical specification and sampling properties of autocorrelation time-series. (Approximation of Eq. 4 is what we know as the standard error of autocorrelation)
- (Brockwell and Davis, 2016) - Introduction to Time Series and Forecasting.