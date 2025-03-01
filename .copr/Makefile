# Makefile for building kwin-effects-forceblur in COPR

COMMIT_ID = 9fb19aafddecb64fa38b1d5f90ab4af809da0cd1
SHORT_COMMIT = $(shell echo $(COMMIT_ID) | cut -c1-7)
SPEC_FILE = kwin-effects-forceblur.spec
SOURCE_URL = https://github.com/taj-ny/kwin-effects-forceblur
NAME = kwin-effects-forceblur
VERSION = 0.1
RELEASE = 1
SOURCES_DIR = $(shell pwd)/sources
BUILD_DIR = $(shell pwd)/build

.PHONY: all srpm clean copr_build local_build

all: srpm

$(SOURCES_DIR):
	mkdir -p $(SOURCES_DIR)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(SOURCES_DIR)/$(NAME)-$(SHORT_COMMIT).tar.gz: | $(SOURCES_DIR)
	curl -L $(SOURCE_URL)/archive/$(COMMIT_ID)/$(NAME)-$(SHORT_COMMIT).tar.gz -o $(SOURCES_DIR)/$(NAME)-$(SHORT_COMMIT).tar.gz

srpm: $(SOURCES_DIR)/$(NAME)-$(SHORT_COMMIT).tar.gz $(SPEC_FILE) | $(BUILD_DIR)
	cp $(SPEC_FILE) $(BUILD_DIR)/
	rpmbuild -bs \
		--define "_sourcedir $(SOURCES_DIR)" \
		--define "_srcrpmdir $(BUILD_DIR)" \
		--define "_rpmdir $(BUILD_DIR)" \
		--define "_builddir $(BUILD_DIR)" \
		$(BUILD_DIR)/$(SPEC_FILE)
	@echo "SRPM built at: $(BUILD_DIR)/$(NAME)-$(VERSION)-$(RELEASE)*.src.rpm"

copr_build: srpm
	copr-cli build myproject $(BUILD_DIR)/$(NAME)-$(VERSION)-$(RELEASE)*.src.rpm

local_build: srpm
	rpmbuild --rebuild $(BUILD_DIR)/$(NAME)-$(VERSION)-$(RELEASE)*.src.rpm

clean:
	rm -rf $(SOURCES_DIR) $(BUILD_DIR)
