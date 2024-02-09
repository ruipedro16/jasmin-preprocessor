# -*- Makefile -*-

JASMIN       ?= jasminc
JFLAGS       ?= -nowarning -g ${JADDFLAGS}
PREPROCESSOR ?= ../preprocessor

SOURCES      := $(wildcard *.jtmpl)
JASMIN_FILES := $(SOURCES:.jtmpl=.jazz) memcmp_arm.jazz
ASM_FILES    := $(JASMIN_FILES:.jazz=.s)
TEX_FILES    := $(JASMIN_FILES:.jazz=.tex)

ARRAY_SIZES := $(shell seq 1 100)

all: $(JASMIN_FILES)

jasmin_files: $(JASMIN_FILES)
asm_files:    $(ASM_FILES)
tex_files:    $(TEX_FILES)

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

.PHONY: clean
clean:
	rm -rf $(JASMIN_FILES) $(ASM_FILES) $(TEX_FILES)
