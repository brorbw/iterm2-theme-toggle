A simple python script for toggling the theme of iterm2 from where ever you want to invoke it.

# Install

### Prerequisites

You will need to allow third party applications to talk to the iterm api. This can be done with cookies and security BUT the api is horribly documented thus there is no security here (Smile and wave boys).
To do this go to

```
Preferences -> General -> Magic -> Toggle "Enable Python API"
```

- iTerm2 3.3.10
  (because macOS and python 2.7 rip)

- python3
- pip3

### 1. Get the source

```sh
git clone https://github.com/brorbw/iterm2-theme-toggle.git [preferred location]
```

### 2. Then you will need to install the dependencies.

```sh
cd /where/you/installed/iterm2-theme-toggle
pipenv install
```

### 3. Last thing you will need is to invoke is

I have a line like this in my .zshrc but you can invoke the script with hammerspoon or whatever is to your liking.

```sh
function toggle-theme() {
	python3 ~/<install-path>/main.py
}
```

If you are experiencing issues like `'iTerm2' module not found`, you can try the following solution

```sh
function toggle-theme() {
	BAK_PIPFILE=$PIPENV_PIPFILE
	PIPENV_PIPFILE=~/Projects/iterm2-theme-toggle/Pipfile exec pipenv run python3 ~/Projects/iterm2-theme-toggle/main.py &
	PIPENV_PIPFILE=$BAK_PIPFILE
	disown
}
```

First time you run the script iTerm2 will prompt you for permissions to you the API. Press always, if you don't want to allow it every time

<img src="https://raw.githubusercontent.com/brorbw/iterm2-theme-toggle/master/pics/image.png"/>

Restart iTerm2 and you are good to go

# Configuration

If you need to change the themes that it toggles between you just need to set the environment variables

```sh
export LIGHT_THEME="Nord light"
export DARK_THEME="Laserwave"
```
