Name:           tunein-cli
Version:        0.3.2
Release:        1%{?dist}
Summary:        CLI for listening to internet radio stations

License:        MIT

BuildArch:      x86_64

Requires: alsa-utils, alsa-lib-devel

%description
Browse and listen to thousands of radio stations across the globe right from your terminal 🌎 📻 🎵✨

%prep
# Prepare the build environment

%build
# Build steps (if any)

%install
mkdir -p %{buildroot}/usr/bin
cp -r %{_sourcedir}/amd64/usr %{buildroot}/

%files
/usr/bin/tunein
