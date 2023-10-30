# HOME_DIR='$HOME/FIELDDAQ-Software-and-Electronics/Granusoft/'
HOME_DIR='$HOME/BYU/Capstone/FIELDAQ-Software-and-Electronics/Granusoft/'
eval HOME_DIR=$HOME_DIR
# /home/natelud/BYU/Capstone/FIELDAQ-Software-and-Electronics/Granusoft/.bashrc

pyreqs() {
  local requirements_file="requirements.txt"
  local file_path="${HOME_DIR}${requirements_file}"
  
  echo "Attempting to change to: ${HOME_DIR}"
  cd "$HOME_DIR"
  if [ -f "$file_path" ]; then
    while read -r package; do
      if [ -n "$package" ]; then
        pip install "$package"
        if [ $? -eq 0 ]; then
          echo "Successfully installed $package"
        else
          echo "Failed to install $package"
        fi
      fi
    done < "$file_path"
    echo "Packages installed successfully."
  else
    echo "Requirements file '$file_path' not found."
  fi
}
