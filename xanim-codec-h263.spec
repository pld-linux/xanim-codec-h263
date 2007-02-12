Summary:	H.263 codec for XAnim
Summary(pl.UTF-8):   Kodek H.263 dla XAnima
Name:		xanim-codec-h263
%ifarch ppc
Version:	1.0
%else
Version:	1.1
%endif
Release:	1
License:	BSD (but no sources available)
Group:		X11/Applications/Graphics
# old dlls at http://xanim.polter.net/dlls/
Source1:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_h263_1.1_linuxELFx86c6.tgz
# Source1-md5:	9a4a48d09d20f124a86737656f0566d3
Source2:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_h263_1.1_linuxELFalphaC6.tgz
# Source2-md5:	e0a776e44e715dc0042ae0c5ba0e0646
Source3:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_h263_1.0_linuxELFppc.tgz
# Source3-md5:	2373fdf259a073506633ff39539e97f7
URL:		http://xanim.polter.net/
Requires:	xanim >= 1:2920
ExclusiveArch:	%{ix86} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
H.263 codec decompression DLL for XAnim.

%description -l pl.UTF-8
Biblioteka do dekompresji kodeka H.263 dla XAnima.

%prep
%ifarch %{ix86}
%setup -q -c -T -a1
%endif
%ifarch alpha
%setup -q -c -T -a2
%endif
%ifarch ppc
%setup -q -c -T -a3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

install vid_h263_*.xa $RPM_BUILD_ROOT%{_libdir}/xanim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc h263.readme
%attr(755,root,root) %{_libdir}/xanim/vid_h263_*.xa
