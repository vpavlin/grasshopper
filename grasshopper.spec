Name:           grasshopper
Version:        0.0.32
Release:        1%{?dist}
Summary:        This will make a Nulecule GO!

License:        LGPLv3+
URL:            https://github.com/goern/grasshopper
Source0:        grasshopper-%{version}.tar.gz

ExclusiveArch:  x86_64
BuildRequires:	golang-bin
BuildRequires:  git
BuildRequires:  asciidoc
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
Requires:       golang

%ifarch x86_64
  %global GOARCH amd64
%endif

%description
This will make a Nulecule GO!

%prep
%setup -q -n %{name}-%{version}

mkdir -p $RPM_BUILD_ROOT/%{_bindir}

%build
GOPATH="$(pwd)"
GOBIN="$GOPATH/bin"
GOOS=linux
GOARCH="%{GOARCH}"
export GOPATH GOBIN GOOS GOARCH

LC_ALL=C PATH="$PATH:$GOBIN" go get github.com/tools/godep
LC_ALL=C PATH="$PATH:$GOBIN" go get github.com/goern/grasshopper
LC_ALL=C PATH="$PATH:$GOBIN" GRASSHOPPER_VERSION=%{version} make
LC_ALL=C PATH="$PATH:$GOBIN" GRASSHOPPER_VERSION=%{version} make doc
a2x -d manpage -f manpage grasshopper.8.asciidoc

%install
cp grasshopper-%{version} $RPM_BUILD_ROOT/%{_bindir}/grasshopper-%{version}
cp -a grasshopper.8 %{buildroot}/%{_mandir}/man8/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)

%attr(0755,-,-) %{_bindir}/grasshopper-%{version}

%doc AUTHORS LICENSE
%doc README.html
%doc %{_mandir}/man8/grasshopper.8*

%post
alternatives --install %{_bindir}/grasshopper grasshopper %{_bindir}/grasshopper-{version} %{alternatives_priority}

%preun
alternatives --remove grasshopper %{_bindir}/grasshopper-%{version}

%changelog
* Mon Nov 09 2015 Christoph Görn <goern@redhat.com> 0.0.32-1
- add some manpagegeneration foo but dont use it (goern@redhat.com)
- add index info (goern@redhat.com)
- fix the Makefile: always require GRASSHOPPER_VERSION set on a `make` call
  (goern@redhat.com)
- disable certificate validation (goern@redhat.com)
- implement nulecule-library index list (goern@redhat.com)

* Mon Nov 09 2015 Christoph Görn <goern@redhat.com>
- add some manpagegeneration foo but dont use it (goern@redhat.com)
- add index info (goern@redhat.com)
- fix the Makefile: always require GRASSHOPPER_VERSION set on a `make` call
  (goern@redhat.com)
- disable certificate validation (goern@redhat.com)
- implement nulecule-library index list (goern@redhat.com)

* Mon Nov 09 2015 Christoph Görn <goern@redhat.com> 0.0.31-1
- add viper based runtimeconfig (goern@redhat.com)

* Mon Nov 09 2015 Christoph Görn <goern@redhat.com> 0.0.30-1
- bounce to 0.0.30 (goern@redhat.com)
- finish adding cobra based commands, flags still missing (goern@redhat.com)
- heavy src reorg (goern@redhat.com)
- move files, this should be more like real go (goern@redhat.com)

* Sun Nov 08 2015 Christoph Görn <goern@redhat.com> 0.0.27rc1-1
- add the provider flag (goern@redhat.com)
- fix travis setup (goern@redhat.com)
- add any deps, even for tests, using godep save ./... (goern@redhat.com)
- add the rest of the commands, lifecycle flags are still missing (goern@redhat.com)
- migrate to cobra (goern@redhat.com)

* Sun Nov 08 2015 Christoph Görn <goern@redhat.com> 0.0.26-1
- add grasshopper image (goern@redhat.com)
- some more on doc (goern@redhat.com)
- update to build with GO 1.5.1 (goern@redhat.com)
- fix the copr releaser (goern@redhat.com)
- change from Markdown to Asciidoc (goern@redhat.com)

* Sun Nov 08 2015 Christoph Görn <goern@redhat.com> 0.0.20-1
- fix some more build path issues (goern@redhat.com)

* Wed Nov 04 2015 Christoph Görn <goern@redhat.com> 0.0.12-1
- add git as a build requirement, due to `go get` (goern@redhat.com)

* Wed Nov 04 2015 Christoph Görn <goern@redhat.com> 0.0.9-1
- add godep as a build step (goern@redhat.com)

* Wed Nov 04 2015 Christoph Görn <goern@redhat.com> 0.0.8-1
- fix a type in .spec (goern@redhat.com)

* Wed Nov 04 2015 Christoph Görn <goern@redhat.com> 0.0.7-1
- new package built with tito

* Wed Nov 04 2015 Christoph Görn <goern@redhat.com>
- move to rel-eng/ (goern@redhat.com)
- add man page (stub) (goern@redhat.com)
- remove the .srpm (goern@redhat.com)

* Tue Nov 03 2015 Christoph Görn <goern@redhat.com> 0.0.5-1
- new package built with tito

* Tue Nov 03 2015 Christoph Görn
- initial RPMification
