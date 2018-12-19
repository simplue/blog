# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
  export ZSH=/home/ho/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="clean"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
source ~/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# config thefuck
eval $(thefuck --alias)
# You can use whatever you want as an alias, like for Mondays:
eval $(thefuck --alias FUCK)

# config pure
fpath=( "$HOME/.zfunctions" $fpath )
autoload -U promptinit; promptinit
prompt pure

alias upmall="cd ~/pacofuture/gitee_mall_web && pipenv run python manage.py runserver 8720"
alias reloadshell="source ~/.zshrc"
alias editshell="nano ~/.zshrc"
alias exportshell="cat ~/.zshrc > ~/personal/fee/sh-script/.zshrc"
alias importshell="cat ~/personal/fee/sh-script/.zshrc > ~/.zshrc; source ~/.zshrc; echo done!"
alias containers="docker ps -a"
alias images="docker images"
alias catp="ps -ef|grep $1"
alias tcpstat="sudo netstat -atpn"
alias nginxconf="cd /etc/nginx/sites-enabled"
alias findbig="sudo find / -size +100M"

# https://gist.github.com/peterjaap/22d06bbd1fd216eaf547
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias .....='cd ../../../../..'

mkcd () {
    mkdir -p -- "$1" &&
      cd -P -- "$1"
}

cleanimages() {
	docker rmi -f $(docker images | grep '<none>' | awk '{print $3}')
}

touchdocker() {
	docker ps && echo
	CONTAINER=$(bash -c 'read -p "Choose a container: " tmp; echo $tmp')
	# vared -p 'What would you like to do?: ' -c tmp
	docker exec -it "$CONTAINER" sh
}

alias lspipenv="ls /usr/local/python"
alias rmpipenv="pipenv --rm && rm -f Pipfile Pipfile.lock"
newpipenv() {
	if [ -z "$1" ]; then
		echo "not version specify."
		return 1
	fi

	version=$1

	# https://stackoverflow.com/questions/18864840/bash-substring-of-a-constant-string
	python_bin="/usr/local/python/$version/bin/python$(expr substr $version 1 1)"
	echo $python_bin

	# pipenv --python $python_bin
	if [ -e $python_bin ]; then 
		pipenv --python $python_bin
	else
		echo "Python $version not install"
		return 1
	fi

	sed -i 's/pypi.org\/simple/mirrors.aliyun.com\/pypi\/simple\//g' Pipfile

	if [ -e "requirements.txt" ]; then 
		echo 'detect requirements.txt installing...'
		pipenv install -r requirements.txt
	fi

	cat Pipfile
	pipenv graph
	pipenv run python -V

	return 0
}

extract (){
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar e $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}
