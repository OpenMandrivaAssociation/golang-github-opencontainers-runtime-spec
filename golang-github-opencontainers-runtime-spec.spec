# http://github.com/opencontainers/runtime-spec

%global goipath         github.com/opencontainers/runtime-spec
%global commit          6e08c6983ef8c2173f10ca09266907d4e9e71716


%gometa -i

Name:           %{goname}
Version:        0.5.0
Release:        0.9%{?dist}
Summary:        Open Container Specifications
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc *.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.5.0-0.8.git6e08c69
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.7.git6e08c69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Troy Dawson <tdawson@redhat.com> - 0.5.0-0.6.git6e08c69
- Cleanup spec file conditionals

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.5.git6e08c69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.4.git6e08c69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.3.git6e08c69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-0.2.git6e08c69
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Apr 26 2016 jchaloup <jchaloup@redhat.com> - 0.5.0-0.1.git6e08c69
- Bump to upstream 6e08c6983ef8c2173f10ca09266907d4e9e71716
  resolves: #1330416

* Tue Apr 12 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git93ca97e
- First package for Fedora
  resolves: #1326274

