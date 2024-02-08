# -*- Makefile -*-

JASMIN       ?= jasminc
JFLAGS       ?= -nowarning -g ${JADDFLAGS}
PREPROCESSOR ?= ../preprocessor

SOURCES      := $(wildcard *.jtmpl)
JASMIN_FILES := $(SOURCES:.jtmpl=.jazz) memcmp_arm.jazz
ASM_FILES    := $(JASMIN_FILES:.jazz=.s)

all: $(JASMIN_FILES)

jasmin_files: $(JASMIN_FILES)
asm_files:    $(ASM_FILES)

memcmp_arm.jazz: memcmp.jtmpl
	$(PREPROCESSOR) -in $< -out $@ --arch="arm-m4"

memcmp_arm.s: memcmp_arm.jazz
	$(JASMIN) $(JFLAGS) -arch arm-m4 $< -o $@

.PRECIOUS: %.jazz
%.jazz: %.jtmpl
	$(PREPROCESSOR) -in $< -out $@

%.s: %.jazz
	$(JASMIN) $(JFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -rf $(JASMIN_FILES) $(ASM_FILES)
