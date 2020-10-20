A simple python script for toggling the theme of iterm2 from where ever you want to invoke it.

# Install

### Prerequisites

You will need to allow third party applications to talk to the iterm api. This can be done with cookies and security BUT the api is horribly documented thus there is no security here (Smile and wave boys).
To do this go to `Preferences -> General -> Magic -> Toggle "Enable Python API"`
(because macOS and python 2.7 rip)

- python3
- pip3

### 1. Get the source

```sh
git clone [preferred location]
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
	python3 ~/.config/iterm2-theme-toggle/main.py
}
```

# Configuration

If you need to change the themes that it toggles between you just need to change the following lines

```python
lightTheme = 'Nord light'
darkTheme = 'Laserwave'
```
