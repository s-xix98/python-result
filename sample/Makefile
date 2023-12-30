# MAKE
# ------------------------------------------------------------------------------------------
TARGET := $(shell find . -type f -name '*.py')

PHONY	:=	all
all: fmt lint
	python3 sample.py

# CODING-STYLE
# ------------------------------------------------------------------------------------------
PHONY	:=	fmt
fmt:
	black $(TARGET) && isort $(TARGET)

PHONY	:=	lint
lint:
	mypy $(TARGET) && pylint $(TARGET)

# etc...
# ------------------------------------------------------------------------------------------
.PHONY: $(PHONY)
