Summary:	Java(TM) Cryptography Extension (JCE)
Summary(pl):	Rozszerzenie kryptograficzne Javy (JCE)
Name:		jce
Version:	1.2.2
%define _ver	%(echo %{version} | tr . -)
Release:	0.1
License:	Sun Binary Code License
Group:		Development/Languages/Java
# download requires registration
Source0:	%{name}%{_ver}.zip
URL:		http://java.sun.com/products/jce/
NoSource:	0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The Java Cryptography Extension (JCE) is a set of packages that
provide a framework and implementations for encryption, key generation
and key agreement, and Message Authentication Code (MAC) algorithms.
Support for encryption includes symmetric, asymmetric, block, and
stream ciphers. The software also supports secure streams and sealed
objects. JCE is designed so that other qualified cryptography
libraries can be plugged in as service providers, and new algorithms
can be added seamlessly. (Qualified providers are signed by a trusted
entity.)
						 
This optional package is provided for Java 1.2.x and 1.3.x. It has been
integrated in Java 1.4.

%description -l pl
JCE (Java Cryptography Extension - rozszerzenie kryptograficzne Javy)
to zbiór pakietów dostarczaj±cych szkieletu i implementacji
szyfrowania, generowania i potwierdzania kluczy oraz algorytmów
uwierzytelniania wiadomo¶ci (Message Authentication Code - MAC).
Obs³ugiwane s± szyfry symetryczne i asymetryczne, blokowe i
strumieniowe. Oprogramowanie obs³uguje tak¿e bezpieczne strumienie
oraz opieczêtowane obiekty. JCE jest zaprojektowane tak, ¿eby inne
kwalifikowane biblioteki kryptograficzne mog³y byæ w³±czane jako
dostarczaj±ce us³ugi, a nowe algorytmy dodawane bez problemu
(kwalifikowane biblioteki dostarczaj±ce s± podpisane przez zaufane
jednostki).

Ten opcjonalny pakiet jest przeznaczony dla Javy 1.2.x i 1.3.x, zosta³
zintegrowany z Jav± 1.4.

%prep
%setup -q -n %{name}%{_ver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
cp lib/%{name}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javalibdir}/%{extension}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{_javalibdir}/%{name}*.jar
