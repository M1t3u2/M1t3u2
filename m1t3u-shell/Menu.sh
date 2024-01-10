#!/bin/bash

#-------------------------- BASIC INFOS --------------------------

## M1t3u  : cybersecurity tool
## Author : M1t3u
## Version: 0.1 -- Beta

#-----------------------------------------------------------------

__version__="0.1 --Beta"

# HOST & PORT 
HOST='127.0.0.1'
PORT='8080'

# ANSI colors (FG & BG)
RED="$(printf '\033[31m')"  GREEN="$(printf '\033[32m')"  ORANGE="$(printf '\033[33m')"  BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"  CYAN="$(printf '\033[36m')"  WHITE="$(printf '\033[37m')" BLACK="$(printf '\033[30m')" 
REDBG="$(printf '\033[41m')"  GREENBG="$(printf '\033[42m')"  ORANGEBG="$(printf '\033[43m')"  BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"  CYANBG="$(printf '\033[46m')"  WHITEBG="$(printf '\033[47m')" BLACKBG="$(printf '\033[40m')"
JAUNE="$(printf '\033[33m')" PINK="$(printf '\033[1;95m')"
RESETBG="$(printf '\e[0m\n')"

# BANNER

banner() {
    cat <<-EOF
        ${ORANGE}
        ${ORANGE} __  __ __ _______ ____  _    _ 
        ${ORANGE}|  \/  /_ |__   __|___ \| |  | |
        ${ORANGE}| \  / || |  | |    __) | |  | |
        ${ORANGE}| |\/| || |  | |   |__ <| |  | |
        ${ORANGE}| |  | || |  | |   ___) | |__| |
        ${ORANGE}|_|  |_||_|  |_|  |____/ \____/  
        ${ORANGE}
        ${ORANGE}                                  ${RED}Version: ${__version__}
        ${GREEN}[${WHITE}-${GREEN}]${CYAN} Tool Created by M1t3u (Hugo.Suzanne)${WHITE}
EOF
}

banner


## Exit message
msg_exit() {
	{ clear; banner; echo; }
	echo -e "${GREENBG}${BLACK} Thank you for using this tool. Have a good day.${RESETBG}\n"
	{ reset_color; exit 0; }
}

## About
about() {
	{ clear; banner; echo; }
	cat <<- EOF
		${GREEN} Author   ${RED}:  ${ORANGE}M1t3u ${RED}[ ${ORANGE} HS${RED}]
		${GREEN} Github   ${RED}:  ${CYAN}https://github.com/M1t3u2 ${RED}[ ${ORANGE}]
		${GREEN} Social   ${RED}:  ${CYAN}
		${GREEN} Version  ${RED}:  ${ORANGE}${__version__}

		${WHITE} ${REDBG}Warning:${RESETBG}
		${CYAN}  This Tool is made for educational purpose 
		  only ${RED}!${WHITE}${CYAN} Author will not be responsible for 
		  any misuse of this toolkit ${RED}!${WHITE}
		
		${WHITE} ${CYANBG}Remerciement spécial à:${RESETBG}
		${GREEN}  Invixey, Strandwald

		${RED}[${WHITE}00${RED}]${ORANGE} Menu Principal     ${RED}[${WHITE}99${RED}]${ORANGE} Sortir

	EOF

	read -p "${RED}[${WHITE}-${RED}]${GREEN} Sélectionner une option: ${BLUE}"
	case $REPLY in 
		99)
			msg_exit;;
		0 | 00)
			echo -ne "\n${GREEN}[${WHITE}+${GREEN}]${CYAN} Retourner au menu principal..."
			{ sleep 1; main_menu; };;
		*)
			echo -ne "\n${RED}[${WHITE}!${RED}]${RED} Option invalide, Réessayez..."
			{ sleep 1; about; };;
	esac
}

## Menu
main_menu() {
    while true; do
        { clear; banner; echo; }
        cat <<-EOF
              ${RED}[${WHITE}::${RED}]${RED} Sélectionner une option. ${RED}[${WHITE}::${RED}]${ORANGE}

            ${BLUE}[${WHITE}01${BLUE}]${ORANGE} Look URL             ${BLUE}[${WHITE}04${BLUE}]${ORANGE} Examinator
            ${BLUE}[${WHITE}02${BLUE}]${ORANGE} Generate Password    ${BLUE}[${WHITE}05${BLUE}]${ORANGE} HTML Body Recreate
            ${BLUE}[${WHITE}03${BLUE}]${ORANGE} VPN                  ${BLUE}[${WHITE}06${BLUE}]${ORANGE} Zphisher
            ${BLUE}[${WHITE}99${BLUE}]${ORANGE} About                ${BLUE}[${WHITE}07${BLUE}]${ORANGE} Lazymux
            ${BLUE}[${WHITE}00${BLUE}]${ORANGE} Exit                 ${BLUE}[${WHITE}08${BLUE}]${ORANGE} Wifite
EOF


        read -p "${RED}[${WHITE}-${RED}]${GREEN} Selectionner une option : ${BLUE}"

        case $REPLY in
            1 | 01)
                look_url;;
            2 | 02)
                passwrd
                python passwrd.py
                sleep 15
                ;;
            3 | 03)
                vpn;;
            99)
                about;;
            0 | 00)
                msg_exit;;
            *)
                echo -ne "\n${RED}[${WHITE}!${RED}]${RED} Invalid Option, Try Again..."
                sleep 1;;
        esac
    done
}

# Start the main menu
main_menu
