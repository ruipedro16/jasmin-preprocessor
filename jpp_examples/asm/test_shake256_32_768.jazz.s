	.att_syntax
	.text
	.p2align	5
	.globl	_test_shake256
	.globl	test_shake256
_test_shake256:
test_shake256:
	movq	%rsp, %rax
	leaq	-856(%rsp), %rsp
	andq	$-8, %rsp
	movq	%rax, 848(%rsp)
	movq	%r15, 800(%rsp)
	movq	%r14, 808(%rsp)
	movq	%r13, 816(%rsp)
	movq	%r12, 824(%rsp)
	movq	%rbp, 832(%rsp)
	movq	%rbx, 840(%rsp)
	movq	$0, %rax
	jmp 	Ltest_shake256$4
Ltest_shake256$5:
	movb	(%rsi,%rax), %cl
	movb	%cl, 32(%rsp,%rax)
	incq	%rax
Ltest_shake256$4:
	cmpq	$768, %rax
	jb  	Ltest_shake256$5
	movq	%rsp, %rax
	leaq	32(%rsp), %rsi
	movb	$31, %cl
	movq	$136, %rdx
	leaq	-248(%rsp), %rsp
	call	L_keccak1600_32_768$1
Ltest_shake256$3:
	leaq	248(%rsp), %rsp
	movq	$0, %rax
	jmp 	Ltest_shake256$1
Ltest_shake256$2:
	movb	(%rsp,%rax), %cl
	movb	%cl, (%rdi,%rax)
	incq	%rax
Ltest_shake256$1:
	cmpq	$32, %rax
	jb  	Ltest_shake256$2
	movq	800(%rsp), %r15
	movq	808(%rsp), %r14
	movq	816(%rsp), %r13
	movq	824(%rsp), %r12
	movq	832(%rsp), %rbp
	movq	840(%rsp), %rbx
	movq	848(%rsp), %rsp
	ret 
L_keccak1600_32_768$1:
	movq	%rax, 8(%rsp)
	movb	%cl, 248(%rsp)
	leaq	48(%rsp), %rax
	xorq	%rcx, %rcx
	movq	%rcx, (%rax)
	movq	%rcx, 8(%rax)
	movq	%rcx, 16(%rax)
	movq	%rcx, 24(%rax)
	movq	%rcx, 32(%rax)
	movq	%rcx, 40(%rax)
	movq	%rcx, 48(%rax)
	movq	%rcx, 56(%rax)
	movq	%rcx, 64(%rax)
	movq	%rcx, 72(%rax)
	movq	%rcx, 80(%rax)
	movq	%rcx, 88(%rax)
	movq	%rcx, 96(%rax)
	movq	%rcx, 104(%rax)
	movq	%rcx, 112(%rax)
	movq	%rcx, 120(%rax)
	movq	%rcx, 128(%rax)
	movq	%rcx, 136(%rax)
	movq	%rcx, 144(%rax)
	movq	%rcx, 152(%rax)
	movq	%rcx, 160(%rax)
	movq	%rcx, 168(%rax)
	movq	%rcx, 176(%rax)
	movq	%rcx, 184(%rax)
	movq	%rcx, 192(%rax)
	movq	$0, %rcx
	movq	$768, %r8
	jmp 	L_keccak1600_32_768$16
L_keccak1600_32_768$17:
	subq	%rdx, %r8
	movq	%rdx, %r9
	shrq	$3, %r9
	movq	$0, %r10
	jmp 	L_keccak1600_32_768$19
L_keccak1600_32_768$20:
	movq	(%rsi,%rcx,8), %r11
	xorq	%r11, (%rax,%r10,8)
	incq	%r10
	incq	%rcx
L_keccak1600_32_768$19:
	cmpq	%r9, %r10
	jb  	L_keccak1600_32_768$20
	movq	%rsi, 16(%rsp)
	movq	%r8, 24(%rsp)
	movq	%rcx, 32(%rsp)
	movq	%rdx, 40(%rsp)
	leaq	-224(%rsp), %rsp
	call	L_keccakf1600$1
L_keccak1600_32_768$18:
	leaq	224(%rsp), %rsp
	movq	16(%rsp), %rsi
	movq	24(%rsp), %r8
	movq	32(%rsp), %rcx
	movq	40(%rsp), %rdx
L_keccak1600_32_768$16:
	cmpq	%rdx, %r8
	jnb 	L_keccak1600_32_768$17
	movb	248(%rsp), %r8b
	movq	%rcx, %r9
	shlq	$3, %r9
	movq	$768, %r10
	subq	%r9, %r10
	shrq	$3, %r10
	movq	$0, %r9
	jmp 	L_keccak1600_32_768$14
L_keccak1600_32_768$15:
	movq	(%rsi,%rcx,8), %r11
	xorq	%r11, (%rax,%r9,8)
	incq	%r9
	incq	%rcx
L_keccak1600_32_768$14:
	cmpq	%r10, %r9
	jb  	L_keccak1600_32_768$15
	shlq	$3, %rcx
	shlq	$3, %r9
	movq	$768, %r10
	subq	%rcx, %r10
	jmp 	L_keccak1600_32_768$12
L_keccak1600_32_768$13:
	movb	(%rsi,%rcx), %r11b
	xorb	%r11b, (%rax,%r9)
	incq	%r9
	incq	%rcx
L_keccak1600_32_768$12:
	cmpq	%r10, %r9
	jb  	L_keccak1600_32_768$13
	xorb	%r8b, (%rax,%r9)
	movq	%rdx, %rcx
	addq	$-1, %rcx
	xorb	$-128, (%rax,%rcx)
	movq	8(%rsp), %rcx
	movq	$0, %r8
	movq	$32, %rsi
	jmp 	L_keccak1600_32_768$7
L_keccak1600_32_768$8:
	subq	%rdx, %rsi
	movq	%rcx, 8(%rsp)
	movq	%r8, 40(%rsp)
	movq	%rsi, 32(%rsp)
	movq	%rdx, 24(%rsp)
	leaq	-224(%rsp), %rsp
	call	L_keccakf1600$1
L_keccak1600_32_768$11:
	leaq	224(%rsp), %rsp
	movq	8(%rsp), %rcx
	movq	40(%rsp), %r8
	movq	32(%rsp), %rsi
	movq	24(%rsp), %rdx
	movq	%rdx, %r9
	shrq	$3, %r9
	movq	$0, %r10
	jmp 	L_keccak1600_32_768$9
L_keccak1600_32_768$10:
	movq	(%rax,%r10,8), %r11
	movq	%r11, (%rcx,%r8,8)
	incq	%r10
	incq	%r8
L_keccak1600_32_768$9:
	cmpq	%r9, %r10
	jb  	L_keccak1600_32_768$10
L_keccak1600_32_768$7:
	cmpq	%rdx, %rsi
	jnbe	L_keccak1600_32_768$8
	movq	%rcx, 24(%rsp)
	movq	%r8, 32(%rsp)
	leaq	-224(%rsp), %rsp
	call	L_keccakf1600$1
L_keccak1600_32_768$6:
	leaq	224(%rsp), %rsp
	movq	24(%rsp), %rcx
	movq	32(%rsp), %rdx
	movq	%rdx, %rsi
	shlq	$3, %rsi
	movq	$32, %r8
	subq	%rsi, %r8
	shrq	$3, %r8
	movq	$0, %rsi
	jmp 	L_keccak1600_32_768$4
L_keccak1600_32_768$5:
	movq	(%rax,%rsi,8), %r9
	movq	%r9, (%rcx,%rdx,8)
	incq	%rsi
	incq	%rdx
L_keccak1600_32_768$4:
	cmpq	%r8, %rsi
	jb  	L_keccak1600_32_768$5
	shlq	$3, %rdx
	shlq	$3, %rsi
	movq	$32, %r8
	subq	%rdx, %r8
	jmp 	L_keccak1600_32_768$2
L_keccak1600_32_768$3:
	movb	(%rax,%rsi), %r9b
	movb	%r9b, (%rcx,%rdx)
	incq	%rsi
	incq	%rdx
L_keccak1600_32_768$2:
	cmpq	%r8, %rsi
	jb  	L_keccak1600_32_768$3
	ret 
L_keccakf1600$1:
	leaq	glob_data + 0(%rip), %rcx
	movq	%rcx, 8(%rsp)
	leaq	32(%rsp), %rcx
	movq	$0, %r11
	jmp 	L_keccakf1600$2
L_keccakf1600$3:
	movq	%r11, 16(%rsp)
	movq	8(%rsp), %rdx
	movq	(%rdx,%r11,8), %rdx
	movq	%rdx, 24(%rsp)
	movq	(%rax), %r10
	movq	8(%rax), %r9
	movq	16(%rax), %rbx
	movq	24(%rax), %rbp
	movq	32(%rax), %r12
	xorq	40(%rax), %r10
	xorq	48(%rax), %r9
	xorq	56(%rax), %rbx
	xorq	64(%rax), %rbp
	xorq	72(%rax), %r12
	xorq	80(%rax), %r10
	xorq	88(%rax), %r9
	xorq	96(%rax), %rbx
	xorq	104(%rax), %rbp
	xorq	112(%rax), %r12
	xorq	120(%rax), %r10
	xorq	128(%rax), %r9
	xorq	136(%rax), %rbx
	xorq	144(%rax), %rbp
	xorq	152(%rax), %r12
	xorq	160(%rax), %r10
	xorq	168(%rax), %r9
	xorq	176(%rax), %rbx
	xorq	184(%rax), %rbp
	xorq	192(%rax), %r12
	movq	%r9, %rdx
	rolq	$1, %rdx
	xorq	%r12, %rdx
	movq	%rbx, %rsi
	rolq	$1, %rsi
	xorq	%r10, %rsi
	movq	%rbp, %r8
	rolq	$1, %r8
	xorq	%r9, %r8
	movq	%r12, %r9
	rolq	$1, %r9
	xorq	%rbx, %r9
	rolq	$1, %r10
	xorq	%rbp, %r10
	movq	(%rax), %rbx
	xorq	%rdx, %rbx
	movq	48(%rax), %rbp
	xorq	%rsi, %rbp
	rolq	$44, %rbp
	movq	96(%rax), %r12
	xorq	%r8, %r12
	rolq	$43, %r12
	movq	144(%rax), %r13
	xorq	%r9, %r13
	rolq	$21, %r13
	movq	192(%rax), %r14
	xorq	%r10, %r14
	rolq	$14, %r14
	andnq	%r12, %rbp, %r15
	xorq	%rbx, %r15
	xorq	24(%rsp), %r15
	movq	%r15, (%rcx)
	andnq	%r13, %r12, %r15
	xorq	%rbp, %r15
	movq	%r15, 8(%rcx)
	andnq	%r14, %r13, %r15
	xorq	%r12, %r15
	movq	%r15, 16(%rcx)
	andnq	%rbx, %r14, %r12
	xorq	%r13, %r12
	movq	%r12, 24(%rcx)
	andnq	%rbp, %rbx, %rbx
	xorq	%r14, %rbx
	movq	%rbx, 32(%rcx)
	movq	24(%rax), %rbx
	xorq	%r9, %rbx
	rolq	$28, %rbx
	movq	72(%rax), %rbp
	xorq	%r10, %rbp
	rolq	$20, %rbp
	movq	80(%rax), %r12
	xorq	%rdx, %r12
	rolq	$3, %r12
	movq	128(%rax), %r13
	xorq	%rsi, %r13
	rolq	$45, %r13
	movq	176(%rax), %r14
	xorq	%r8, %r14
	rolq	$61, %r14
	andnq	%r12, %rbp, %r15
	xorq	%rbx, %r15
	movq	%r15, 40(%rcx)
	andnq	%r13, %r12, %r15
	xorq	%rbp, %r15
	movq	%r15, 48(%rcx)
	andnq	%r14, %r13, %r15
	xorq	%r12, %r15
	movq	%r15, 56(%rcx)
	andnq	%rbx, %r14, %r12
	xorq	%r13, %r12
	movq	%r12, 64(%rcx)
	andnq	%rbp, %rbx, %rbx
	xorq	%r14, %rbx
	movq	%rbx, 72(%rcx)
	movq	8(%rax), %rbx
	xorq	%rsi, %rbx
	rolq	$1, %rbx
	movq	56(%rax), %rbp
	xorq	%r8, %rbp
	rolq	$6, %rbp
	movq	104(%rax), %r12
	xorq	%r9, %r12
	rolq	$25, %r12
	movq	152(%rax), %r13
	xorq	%r10, %r13
	rolq	$8, %r13
	movq	160(%rax), %r14
	xorq	%rdx, %r14
	rolq	$18, %r14
	andnq	%r12, %rbp, %r15
	xorq	%rbx, %r15
	movq	%r15, 80(%rcx)
	andnq	%r13, %r12, %r15
	xorq	%rbp, %r15
	movq	%r15, 88(%rcx)
	andnq	%r14, %r13, %r15
	xorq	%r12, %r15
	movq	%r15, 96(%rcx)
	andnq	%rbx, %r14, %r12
	xorq	%r13, %r12
	movq	%r12, 104(%rcx)
	andnq	%rbp, %rbx, %rbx
	xorq	%r14, %rbx
	movq	%rbx, 112(%rcx)
	movq	32(%rax), %rbx
	xorq	%r10, %rbx
	rolq	$27, %rbx
	movq	40(%rax), %rbp
	xorq	%rdx, %rbp
	rolq	$36, %rbp
	movq	88(%rax), %r12
	xorq	%rsi, %r12
	rolq	$10, %r12
	movq	136(%rax), %r13
	xorq	%r8, %r13
	rolq	$15, %r13
	movq	184(%rax), %r14
	xorq	%r9, %r14
	rolq	$56, %r14
	andnq	%r12, %rbp, %r15
	xorq	%rbx, %r15
	movq	%r15, 120(%rcx)
	andnq	%r13, %r12, %r15
	xorq	%rbp, %r15
	movq	%r15, 128(%rcx)
	andnq	%r14, %r13, %r15
	xorq	%r12, %r15
	movq	%r15, 136(%rcx)
	andnq	%rbx, %r14, %r12
	xorq	%r13, %r12
	movq	%r12, 144(%rcx)
	andnq	%rbp, %rbx, %rbx
	xorq	%r14, %rbx
	movq	%rbx, 152(%rcx)
	movq	16(%rax), %rbx
	xorq	%r8, %rbx
	rolq	$62, %rbx
	movq	64(%rax), %r8
	xorq	%r9, %r8
	rolq	$55, %r8
	movq	112(%rax), %r9
	xorq	%r10, %r9
	rolq	$39, %r9
	movq	120(%rax), %r10
	xorq	%rdx, %r10
	rolq	$41, %r10
	movq	168(%rax), %rdx
	xorq	%rsi, %rdx
	rolq	$2, %rdx
	andnq	%r9, %r8, %rsi
	xorq	%rbx, %rsi
	movq	%rsi, 160(%rcx)
	andnq	%r10, %r9, %rsi
	xorq	%r8, %rsi
	movq	%rsi, 168(%rcx)
	andnq	%rdx, %r10, %rsi
	xorq	%r9, %rsi
	movq	%rsi, 176(%rcx)
	andnq	%rbx, %rdx, %rsi
	xorq	%r10, %rsi
	movq	%rsi, 184(%rcx)
	andnq	%r8, %rbx, %rsi
	xorq	%rdx, %rsi
	movq	%rsi, 192(%rcx)
	movq	8(%rsp), %rdx
	movq	8(%rdx,%r11,8), %rdx
	movq	%rdx, 24(%rsp)
	movq	(%rcx), %r10
	movq	8(%rcx), %r9
	movq	16(%rcx), %r11
	movq	24(%rcx), %rbx
	movq	32(%rcx), %rbp
	xorq	40(%rcx), %r10
	xorq	48(%rcx), %r9
	xorq	56(%rcx), %r11
	xorq	64(%rcx), %rbx
	xorq	72(%rcx), %rbp
	xorq	80(%rcx), %r10
	xorq	88(%rcx), %r9
	xorq	96(%rcx), %r11
	xorq	104(%rcx), %rbx
	xorq	112(%rcx), %rbp
	xorq	120(%rcx), %r10
	xorq	128(%rcx), %r9
	xorq	136(%rcx), %r11
	xorq	144(%rcx), %rbx
	xorq	152(%rcx), %rbp
	xorq	160(%rcx), %r10
	xorq	168(%rcx), %r9
	xorq	176(%rcx), %r11
	xorq	184(%rcx), %rbx
	xorq	192(%rcx), %rbp
	movq	%r9, %rdx
	rolq	$1, %rdx
	xorq	%rbp, %rdx
	movq	%r11, %rsi
	rolq	$1, %rsi
	xorq	%r10, %rsi
	movq	%rbx, %r8
	rolq	$1, %r8
	xorq	%r9, %r8
	movq	%rbp, %r9
	rolq	$1, %r9
	xorq	%r11, %r9
	rolq	$1, %r10
	xorq	%rbx, %r10
	movq	(%rcx), %r11
	xorq	%rdx, %r11
	movq	48(%rcx), %rbx
	xorq	%rsi, %rbx
	rolq	$44, %rbx
	movq	96(%rcx), %rbp
	xorq	%r8, %rbp
	rolq	$43, %rbp
	movq	144(%rcx), %r12
	xorq	%r9, %r12
	rolq	$21, %r12
	movq	192(%rcx), %r13
	xorq	%r10, %r13
	rolq	$14, %r13
	andnq	%rbp, %rbx, %r14
	xorq	%r11, %r14
	xorq	24(%rsp), %r14
	movq	%r14, (%rax)
	andnq	%r12, %rbp, %r14
	xorq	%rbx, %r14
	movq	%r14, 8(%rax)
	andnq	%r13, %r12, %r14
	xorq	%rbp, %r14
	movq	%r14, 16(%rax)
	andnq	%r11, %r13, %rbp
	xorq	%r12, %rbp
	movq	%rbp, 24(%rax)
	andnq	%rbx, %r11, %r11
	xorq	%r13, %r11
	movq	%r11, 32(%rax)
	movq	24(%rcx), %r11
	xorq	%r9, %r11
	rolq	$28, %r11
	movq	72(%rcx), %rbx
	xorq	%r10, %rbx
	rolq	$20, %rbx
	movq	80(%rcx), %rbp
	xorq	%rdx, %rbp
	rolq	$3, %rbp
	movq	128(%rcx), %r12
	xorq	%rsi, %r12
	rolq	$45, %r12
	movq	176(%rcx), %r13
	xorq	%r8, %r13
	rolq	$61, %r13
	andnq	%rbp, %rbx, %r14
	xorq	%r11, %r14
	movq	%r14, 40(%rax)
	andnq	%r12, %rbp, %r14
	xorq	%rbx, %r14
	movq	%r14, 48(%rax)
	andnq	%r13, %r12, %r14
	xorq	%rbp, %r14
	movq	%r14, 56(%rax)
	andnq	%r11, %r13, %rbp
	xorq	%r12, %rbp
	movq	%rbp, 64(%rax)
	andnq	%rbx, %r11, %r11
	xorq	%r13, %r11
	movq	%r11, 72(%rax)
	movq	8(%rcx), %r11
	xorq	%rsi, %r11
	rolq	$1, %r11
	movq	56(%rcx), %rbx
	xorq	%r8, %rbx
	rolq	$6, %rbx
	movq	104(%rcx), %rbp
	xorq	%r9, %rbp
	rolq	$25, %rbp
	movq	152(%rcx), %r12
	xorq	%r10, %r12
	rolq	$8, %r12
	movq	160(%rcx), %r13
	xorq	%rdx, %r13
	rolq	$18, %r13
	andnq	%rbp, %rbx, %r14
	xorq	%r11, %r14
	movq	%r14, 80(%rax)
	andnq	%r12, %rbp, %r14
	xorq	%rbx, %r14
	movq	%r14, 88(%rax)
	andnq	%r13, %r12, %r14
	xorq	%rbp, %r14
	movq	%r14, 96(%rax)
	andnq	%r11, %r13, %rbp
	xorq	%r12, %rbp
	movq	%rbp, 104(%rax)
	andnq	%rbx, %r11, %r11
	xorq	%r13, %r11
	movq	%r11, 112(%rax)
	movq	32(%rcx), %r11
	xorq	%r10, %r11
	rolq	$27, %r11
	movq	40(%rcx), %rbx
	xorq	%rdx, %rbx
	rolq	$36, %rbx
	movq	88(%rcx), %rbp
	xorq	%rsi, %rbp
	rolq	$10, %rbp
	movq	136(%rcx), %r12
	xorq	%r8, %r12
	rolq	$15, %r12
	movq	184(%rcx), %r13
	xorq	%r9, %r13
	rolq	$56, %r13
	andnq	%rbp, %rbx, %r14
	xorq	%r11, %r14
	movq	%r14, 120(%rax)
	andnq	%r12, %rbp, %r14
	xorq	%rbx, %r14
	movq	%r14, 128(%rax)
	andnq	%r13, %r12, %r14
	xorq	%rbp, %r14
	movq	%r14, 136(%rax)
	andnq	%r11, %r13, %rbp
	xorq	%r12, %rbp
	movq	%rbp, 144(%rax)
	andnq	%rbx, %r11, %r11
	xorq	%r13, %r11
	movq	%r11, 152(%rax)
	movq	16(%rcx), %r11
	xorq	%r8, %r11
	rolq	$62, %r11
	movq	64(%rcx), %r8
	xorq	%r9, %r8
	rolq	$55, %r8
	movq	112(%rcx), %r9
	xorq	%r10, %r9
	rolq	$39, %r9
	movq	120(%rcx), %r10
	xorq	%rdx, %r10
	rolq	$41, %r10
	movq	168(%rcx), %rdx
	xorq	%rsi, %rdx
	rolq	$2, %rdx
	andnq	%r9, %r8, %rsi
	xorq	%r11, %rsi
	movq	%rsi, 160(%rax)
	andnq	%r10, %r9, %rsi
	xorq	%r8, %rsi
	movq	%rsi, 168(%rax)
	andnq	%rdx, %r10, %rsi
	xorq	%r9, %rsi
	movq	%rsi, 176(%rax)
	andnq	%r11, %rdx, %rsi
	xorq	%r10, %rsi
	movq	%rsi, 184(%rax)
	andnq	%r8, %r11, %rsi
	xorq	%rdx, %rsi
	movq	%rsi, 192(%rax)
	movq	16(%rsp), %r11
	addq	$2, %r11
L_keccakf1600$2:
	cmpq	$23, %r11
	jb  	L_keccakf1600$3
	ret 
	.data
	.p2align	5
_glob_data:
glob_data:
      .byte 1
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -126
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -118
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte 0
      .byte -128
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte -117
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 1
      .byte 0
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -127
      .byte -128
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte 9
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte -118
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -120
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 9
      .byte -128
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 10
      .byte 0
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -117
      .byte -128
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -117
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte -119
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte 3
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte 2
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte 10
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 10
      .byte 0
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte -127
      .byte -128
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte -128
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte -128
      .byte 1
      .byte 0
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte 0
      .byte 8
      .byte -128
      .byte 0
      .byte -128
      .byte 0
      .byte 0
      .byte 0
      .byte -128
