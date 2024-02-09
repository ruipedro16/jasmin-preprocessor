# -*- Makefile -*-

JASMIN       ?= jasminc
JFLAGS       ?= -nowarning -g ${JADDFLAGS}
PREPROCESSOR ?= ../preprocessor

SOURCES            := $(wildcard *.jtmpl)
JASMIN_FILES       := $(SOURCES:.jtmpl=.jazz) memcmp_arm.jazz
ASM_FILES          := $(JASMIN_FILES:.jazz=.s)
EASYCRYPT_FILES    := map_add_1.ec memcmp.ec memcmp_arm.ec memcpy.ec rec_sum.ec
TEX_FILES          := $(JASMIN_FILES:.jazz=.tex)

all: $(JASMIN_FILES)

jasmin_files:    $(JASMIN_FILES)
easycrypt_files: $(EASYCRYPT_FILES)
asm_files:       $(ASM_FILES)
tex_files:       $(TEX_FILES)

%_arm.jazz: %.jtmpl
	$(PREPROCESSOR) -in $< -out $@ --arch="arm-m4"

%_arm.s: %_arm.jazz
	$(JASMIN) $(JFLAGS) -arch arm-m4 $< -o $@

.PRECIOUS: %.jazz
%.jazz: %.jtmpl
	$(PREPROCESSOR) -in $< -out $@

%.s: %.jazz
	$(JASMIN) $(JFLAGS) $< -o $@

%_arm.tex: %_arm.jazz
	jazz2tex $< --arch arm-m4 --output $@

%.tex: %.jazz
	jazz2tex $< --output $@

map_add_1.ec: map_add_1.jazz
	$(JASMIN) -oec $@ -ec map_add_1_4 $<

memcmp.ec: memcmp.jazz
	$(JASMIN) -oec $@ -ec memcmp $<

memcmp_arm.ec: memcmp_arm.jazz
	$(JASMIN) -arch arm-m4 -oec $@ -ec memcmp $<

memcpy.ec: memcpy.jazz
	$(JASMIN) -oec $@ -ec __memcpy_3_u8 $<

rec_sum.ec: rec_sum.jazz
	$(JASMIN) -oec $@ -ec sum_array_10 $<

u32_to_u64.ec: u32_to_u64.jazz
	$(JASMIN) -oec $@ -ec __wordsize1_to_wordsize2_3_u64_u32 $<

.PHONY: clean
clean:
	rm -rf $(ASM_FILES) $(TEX_FILES) *.ec
