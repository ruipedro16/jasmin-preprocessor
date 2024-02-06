# -*- Makefile -*-

JASMIN       ?= jasminc
JFLAGS       ?= -nowarning -g ${JADDFLAGS}
PREPROCESSOR ?= ../preprocessor

.PRECIOUS: %.jazz
%.jazz: %.jtmpl
	$(PREPROCESSOR) -in $< -out $@

%.s: %.jazz
	$(JASMIN) $(JFLAGS) $< -o $@

SOURCES      := $(wildcard *.jtmpl)
JASMIN_FILES := $(SOURCES:.jtmpl=.jazz)
ASM_FILES    := $(SOURCES:.jtmpl=.s)

all: $(JASMIN_FILES) $(ASM_FILES)

jasmin_files: $(JASMIN_FILES)
asm_files:    $(ASM_FILES)

.PHONY: clean
clean:
	rm -rf $(JASMIN_FILES) $(ASM_FILES)
