if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi

PS1='\e[92mPlusX HK\[\033[91m\]@\[\033[93m\]\t\[\033[91m\] •\[\033[01;92m\]>> \[\033[93m\]\w\[\033[00;93m\]\[\033[92m\]:
\033[93m\]└╼\[\033[01;92m\]•>> \033[01;92m'
clear
neofetch --logo
