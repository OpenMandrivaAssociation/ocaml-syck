Name:           ocaml-syck
Version:        0.1.1
Release:        %mkrel 1
Summary:        Syck bindings for OCaml, allowing to read and write YAML files
License:        MIT
Group:          Development/Other
URL:            http://ocaml-syck.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ocaml-syck/ocaml-syck-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       ocaml
Requires:       libsyck0
BuildRequires:  libsyck-devel
BuildRequires:  ocaml-findlib

%description
The ocaml-syck library provides Syck bindings for OCaml,
allowing an OCaml program to read and write YAML files.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
make OBJ=cmo LIB=cma OCAMLC=ocamlc
make OBJ=cmx LIB=cmxa
pushd yaml
mkdir -p doc
ocamldoc -colorize-code -html yamlNode.mli yamlParser.mli -d doc
popd
mv yaml/doc .

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocamlfind install syck yaml/{META,*.mli,*.cmi,*.cma,*.a,*.cmxa,*.cmx,dll*.so}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%dir %{_libdir}/ocaml/syck
%{_libdir}/ocaml/syck/META
%{_libdir}/ocaml/syck/*.cma
%{_libdir}/ocaml/syck/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc TODO
%doc doc
%{_libdir}/ocaml/syck/*.a
%{_libdir}/ocaml/syck/*.cmxa
%{_libdir}/ocaml/syck/*.cmx
%{_libdir}/ocaml/syck/*.mli
