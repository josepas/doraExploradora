
function trapear {
    trap insultar SIGHUP
    trap insultar SIGINT
    trap insultar SIGQUIT
    trap insultar SIGILL
    trap insultar SIGTRAP
    trap insultar SIGABRT
    trap insultar SIGBUS
    trap insultar SIGFPE
#
    trap insultar SIGUSR1
    trap insultar SIGSEGV
    trap insultar SIGUSR2
    trap insultar SIGPIPE
    trap insultar SIGALRM
    trap insultar SIGTERM
    # trap insultar SIGSTKFLT
    # trap insultar SIGCHLD
    # trap insultar SIGCONT
    trap insultar SIGSTOP
    trap insultar SIGTSTP
    # trap insultar SIGTTIN
    # trap insultar SIGTTOU
    # trap insultar SIGURG
    # trap insultar SIGXCPU
    # trap insultar SIGXFSZ
    # trap insultar SIGVTALRM
    # trap insultar SIGPROF
    # trap insultar SIGWINCH
    # trap insultar SIGIO
    # trap insultar SIGPWR
    # trap insultar SIGSYS
    # trap insultar SIGRTMIN
    # trap insultar SIGRTMIN+1
    # trap insultar SIGRTMIN+2
    # trap insultar SIGRTMIN+3
    # trap insultar SIGRTMIN+4
    # trap insultar SIGRTMIN+5
    # trap insultar SIGRTMIN+6
    # trap insultar SIGRTMIN+7
    # trap insultar SIGRTMIN+8
    # trap insultar SIGRTMIN+9
    # trap insultar SIGRTMIN+10
    # trap insultar SIGRTMIN+11
    # trap insultar SIGRTMIN+12
    # trap insultar SIGRTMIN+13
    # trap insultar SIGRTMIN+14
    # trap insultar SIGRTMIN+15
    # trap insultar SIGRTMAX-14
    # trap insultar SIGRTMAX-13
    # trap insultar SIGRTMAX-12
    # trap insultar SIGRTMAX-11
    # trap insultar SIGRTMAX-10
    # trap insultar SIGRTMAX-9
    # trap insultar SIGRTMAX-8
    # trap insultar SIGRTMAX-7
    # trap insultar SIGRTMAX-6
    # trap insultar SIGRTMAX-5
    # trap insultar SIGRTMAX-4
    # trap insultar SIGRTMAX-3
    # trap insultar SIGRTMAX-2
    # trap insultar SIGRTMAX-1
    # trap insultar SIGRTMAX
    echo ""
}

function go_evil {
    clear
    echo "Hola preprador, mi PID es: $$"
    sleep 3
    cat ascciDora/zorro2
    trapear    
    while true
        do
        p=""
    done
}

function insultar {
    clear
    echo "Hola preprador, mi PID es: $$"
    echo "ME LLEVARE TUS COSAS!!!"
    sleep 0.3
    cat ascciDora/zorro2
}

go_evil