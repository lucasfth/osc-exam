def main():
    D = 2
    S = 3
    rdi = D                 # irmovq $D, %rdi
    rsi = S                 # irmovq $S, %rsi
    rax = 2                 # irmowq two, %rax  # mrmovq 0(%rax), %rax

    while (True):           # main
        rax += rdi          # addq %rdi, %rax
        rax *= 2            # addq %rax, %rax
        rsi -= rdi          # subq %rdi, %rsi
        if (rsi == 0):      # je done
            break

    print(rax)


main()
