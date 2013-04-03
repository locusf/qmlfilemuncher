# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       qmlfilemuncher

# >> macros
# << macros

Summary:    File Manager for Nemo
Version:    0.0.9
Release:    1
Group:      Applications/System
License:    BSD
URL:        https://github.com/nemomobile/qmlfilemuncher
Source0:    %{name}-%{version}.tar.bz2
Source100:  qmlfilemuncher.yaml
Requires:   qt-components
Requires:   nemo-qml-plugins-thumbnailer
Requires:   nemo-qml-plugins-folderlistmodel
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(qdeclarative-boostable)
BuildRequires:  desktop-file-utils

%description
File Manager using Qt Quick Components for Nemo Mobile.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/qmlfilemuncher
%{_datadir}/applications/qmlfilemuncher.desktop
%{_datadir}/themes/base/meegotouch/icons/icons-Applications-filemanager.png
%{_libdir}/qt4/imports/org/nemomobile/qmlfilemuncher/*
# >> files
# << files
