Name:      libhybris	
Version:   0.0.0
Release:   1%{?dist}
Summary:   Hybris allowing us to use bionic-based HW adaptations in glibc systems

Group:	   System
License:   Apache 2.0
URL:	   https://github.com/libhybris/libhybris
Source0:   %{name}-%{version}.tar.bz2
BuildRequires: libtool

%description
%{summary}.

%package devel
Summary: common development headers for libhybris
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package libEGL
Summary: EGL for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libEGL
Provides: libEGL.so.1

%description libEGL
%{summary}.

%package libEGL-devel
Summary: EGL development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libEGL-devel

%description libEGL-devel
%{summary}.

%package libGLESv1
Summary: GLESv1 for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLESv1
Provides: libGLES_CM.so.1

%description libGLESv1
%{summary}.

%package libGLESv1-devel
Summary: GLESv1 development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libGLESv1 = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libGLESv1-devel

%description libGLESv1-devel
%{summary}.

%package libGLESv2
Summary: GLESv2 for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLESv2
Provides: libGLESv2.so.2

%description libGLESv2
%{summary}.

%package libGLESv2-devel
Summary: GLESv2 development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libGLESv2 = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libGLESv2-devel

%description libGLESv2-devel
%{summary}.

%package libOpenCL
Summary: OpenCL for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libOpenCL

%description libOpenCL
%{summary}.

%package libOpenCL-devel
Summary: OpenVG development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libOpenCL = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libOpenCL-devel

%description libOpenCL-devel
%{summary}.

%package libOpenVG
Summary: OpenVG for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libOpenVG

%description libOpenVG
%{summary}.

%package libOpenVG-devel
Summary: OpenVG development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libOpenVG = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libOpenVG-devel

%description libOpenVG-devel
%{summary}.

%package libhardware
Summary: libhardware wrapping of libhybris
Group:   System

%description libhardware
%{summary}.

%package libhardware-devel
Summary: libhardware wrapping of libhybris
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Group:   System

%description libhardware-devel
%{summary}.

%package tests
Summary: Tests for %{name}
Group:   System

%description tests
%{summary}.

%prep
%setup -q

%build
cd hybris
autoreconf -v -f -i
%configure \
%ifarch %{arm}
--enable-arch=arm \
%endif
%ifarch %{ix86}
--enable-arch=x86 \
%endif
%{nil}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd hybris
make install DESTDIR=$RPM_BUILD_ROOT

# Remove the static libraries.
rm %{buildroot}/%{_libdir}/*.la
# No need for libui for Mer
rm %{buildroot}/%{_libdir}/libui.*

%files
%defattr(-,root,root,-)
%{_libdir}/libhybris-common.so.1
%{_libdir}/libhybris-common.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/android/cutils/native_handle.h
%{_includedir}/android/system/graphics.h
%{_includedir}/android/system/window.h
%{_libdir}/libhybris-common.so

%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.1
%{_libdir}/libEGL.so.1.0.0

%files libEGL-devel
%defattr(-,root,root,-)
%{_includedir}/KHR/*.h
%{_includedir}/EGL/*.h
%{_libdir}/libEGL.so

%files libGLESv1
%defattr(-,root,root,-)

%files libGLESv1-devel
%defattr(-,root,root,-)
%{_includedir}/GLES/*.h

%files libGLESv2
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so.2
%{_libdir}/libGLESv2.so.2.0.0

%files libGLESv2-devel
%defattr(-,root,root,-)
%{_includedir}/GLES2/*.h
%{_libdir}/libGLESv2.so

%files libOpenCL
%defattr(-,root,root,-)

%files libOpenCL-devel
%defattr(-,root,root,-)
%{_includedir}/CL/cl.h
%{_includedir}/CL/cl.hpp
%{_includedir}/CL/cl_ext.h
%{_includedir}/CL/cl_gl.h
%{_includedir}/CL/cl_gl_ext.h
%{_includedir}/CL/cl_platform.h
%{_includedir}/CL/opencl.h

%files libOpenVG
%defattr(-,root,root,-)
%{_includedir}/VG/openvg.h
%{_includedir}/VG/vgext.h
%{_includedir}/VG/vgplatform.h
%{_includedir}/VG/vgu.h

%files libOpenVG-devel
%defattr(-,root,root,-)
%{_includedir}/GLES2/*.h
%{_libdir}/libGLESv2.so

%files libhardware
%defattr(-,root,root,-)
%{_libdir}/libhardware.so.2
%{_libdir}/libhardware.so.2.0.0

%files libhardware-devel
%defattr(-,root,root,-)
%{_libdir}/libhardware.so
%{_includedir}/android/hardware/fb.h
%{_includedir}/android/hardware/gralloc.h
%{_includedir}/android/hardware/hardware.h
%{_includedir}/android/hardware/lights.h
%{_includedir}/android/hardware/sensors.h

%files tests
%defattr(-,root,root,-)
%{_bindir}/test_egl
%{_bindir}/test_glesv2
%{_bindir}/test_lights
%{_bindir}/test_offscreen_rendering
%{_bindir}/test_sensors
%{_bindir}/test_ui

