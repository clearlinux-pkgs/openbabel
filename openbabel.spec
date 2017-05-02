#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openbabel
Version  : 2.4.1
Release  : 2
URL      : https://downloads.sourceforge.net/project/openbabel/openbabel/2.4.1/openbabel-2.4.1.tar.gz
Source0  : https://downloads.sourceforge.net/project/openbabel/openbabel/2.4.1/openbabel-2.4.1.tar.gz
Summary  : R interface to OpenBabel
Group    : Development/Tools
License  : GPL-2.0
Requires: openbabel-bin
Requires: openbabel-lib
Requires: openbabel-doc
Requires: openbabel-data
BuildRequires : cairo-dev
BuildRequires : cmake
BuildRequires : eigen-data
BuildRequires : eigen-dev
BuildRequires : libxml2-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zlib-dev

%description
Open Babel Tools, version 2.3.2
-----------------------
This directory contains a selection of ready-to-use tools for a
variety of tasks in molecular modeling, cheminformatics, and related
areas. Most are designed as command-line utilies for any operating
system.

%package bin
Summary: bin components for the openbabel package.
Group: Binaries
Requires: openbabel-data

%description bin
bin components for the openbabel package.


%package data
Summary: data components for the openbabel package.
Group: Data

%description data
data components for the openbabel package.


%package dev
Summary: dev components for the openbabel package.
Group: Development
Requires: openbabel-lib
Requires: openbabel-bin
Requires: openbabel-data
Provides: openbabel-devel

%description dev
dev components for the openbabel package.


%package doc
Summary: doc components for the openbabel package.
Group: Documentation

%description doc
doc components for the openbabel package.


%package lib
Summary: lib components for the openbabel package.
Group: Libraries
Requires: openbabel-data

%description lib
lib components for the openbabel package.


%prep
%setup -q -n openbabel-2.4.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485130155
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd clr-build ; make test ; popd

%install
export SOURCE_DATE_EPOCH=1485130155
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/cmake/openbabel2/OpenBabel2Config.cmake
/usr/lib64/cmake/openbabel2/OpenBabel2ConfigVersion.cmake
/usr/lib64/cmake/openbabel2/OpenBabel2_EXPORTS-relwithdebinfo.cmake
/usr/lib64/cmake/openbabel2/OpenBabel2_EXPORTS.cmake

%files bin
%defattr(-,root,root,-)
/usr/bin/babel
/usr/bin/obabel
/usr/bin/obchiral
/usr/bin/obconformer
/usr/bin/obdistgen
/usr/bin/obenergy
/usr/bin/obfit
/usr/bin/obgen
/usr/bin/obgrep
/usr/bin/obminimize
/usr/bin/obprobe
/usr/bin/obprop
/usr/bin/obrms
/usr/bin/obrotamer
/usr/bin/obrotate
/usr/bin/obspectrophore
/usr/bin/obsym
/usr/bin/obtautomer
/usr/bin/obthermo
/usr/bin/roundtrip

%files data
%defattr(-,root,root,-)
/usr/share/openbabel/2.4.1/MACCS.txt
/usr/share/openbabel/2.4.1/SMARTS_InteLigand.txt
/usr/share/openbabel/2.4.1/UFF.prm
/usr/share/openbabel/2.4.1/aromatic.txt
/usr/share/openbabel/2.4.1/atomization-energies.txt
/usr/share/openbabel/2.4.1/atomtyp.txt
/usr/share/openbabel/2.4.1/babel_povray3.inc
/usr/share/openbabel/2.4.1/bondtyp.txt
/usr/share/openbabel/2.4.1/eem.txt
/usr/share/openbabel/2.4.1/eem2015ba.txt
/usr/share/openbabel/2.4.1/eem2015bm.txt
/usr/share/openbabel/2.4.1/eem2015bn.txt
/usr/share/openbabel/2.4.1/eem2015ha.txt
/usr/share/openbabel/2.4.1/eem2015hm.txt
/usr/share/openbabel/2.4.1/eem2015hn.txt
/usr/share/openbabel/2.4.1/element.txt
/usr/share/openbabel/2.4.1/eqeqIonizations.txt
/usr/share/openbabel/2.4.1/fragments.txt
/usr/share/openbabel/2.4.1/gaff.dat
/usr/share/openbabel/2.4.1/gaff.prm
/usr/share/openbabel/2.4.1/ghemical.prm
/usr/share/openbabel/2.4.1/isotope-small.txt
/usr/share/openbabel/2.4.1/isotope.txt
/usr/share/openbabel/2.4.1/logp.txt
/usr/share/openbabel/2.4.1/mmff94.ff
/usr/share/openbabel/2.4.1/mmff94s.ff
/usr/share/openbabel/2.4.1/mmffang.par
/usr/share/openbabel/2.4.1/mmffbndk.par
/usr/share/openbabel/2.4.1/mmffbond.par
/usr/share/openbabel/2.4.1/mmffchg.par
/usr/share/openbabel/2.4.1/mmffdef.par
/usr/share/openbabel/2.4.1/mmffdfsb.par
/usr/share/openbabel/2.4.1/mmffoop.par
/usr/share/openbabel/2.4.1/mmffpbci.par
/usr/share/openbabel/2.4.1/mmffprop.par
/usr/share/openbabel/2.4.1/mmffs_oop.par
/usr/share/openbabel/2.4.1/mmffs_tor.par
/usr/share/openbabel/2.4.1/mmffstbn.par
/usr/share/openbabel/2.4.1/mmfftor.par
/usr/share/openbabel/2.4.1/mmffvdw.par
/usr/share/openbabel/2.4.1/mpC.txt
/usr/share/openbabel/2.4.1/mr.txt
/usr/share/openbabel/2.4.1/patterns.txt
/usr/share/openbabel/2.4.1/phmodel.txt
/usr/share/openbabel/2.4.1/plugindefines.txt
/usr/share/openbabel/2.4.1/psa.txt
/usr/share/openbabel/2.4.1/qeq.txt
/usr/share/openbabel/2.4.1/resdata.txt
/usr/share/openbabel/2.4.1/ringtyp.txt
/usr/share/openbabel/2.4.1/space-groups.txt
/usr/share/openbabel/2.4.1/splash.png
/usr/share/openbabel/2.4.1/superatom.txt
/usr/share/openbabel/2.4.1/svgformat.script
/usr/share/openbabel/2.4.1/templates.sdf
/usr/share/openbabel/2.4.1/torlib.txt
/usr/share/openbabel/2.4.1/types.txt

%files dev
%defattr(-,root,root,-)
/usr/include/inchi/inchi_api.h
/usr/include/openbabel-2.0/openbabel/alias.h
/usr/include/openbabel-2.0/openbabel/atom.h
/usr/include/openbabel-2.0/openbabel/atomclass.h
/usr/include/openbabel-2.0/openbabel/babelconfig.h
/usr/include/openbabel-2.0/openbabel/base.h
/usr/include/openbabel-2.0/openbabel/bitvec.h
/usr/include/openbabel-2.0/openbabel/bond.h
/usr/include/openbabel-2.0/openbabel/bondtyper.h
/usr/include/openbabel-2.0/openbabel/builder.h
/usr/include/openbabel-2.0/openbabel/canon.h
/usr/include/openbabel-2.0/openbabel/chains.h
/usr/include/openbabel-2.0/openbabel/chargemodel.h
/usr/include/openbabel-2.0/openbabel/chemdrawcdx.h
/usr/include/openbabel-2.0/openbabel/chiral.h
/usr/include/openbabel-2.0/openbabel/conformersearch.h
/usr/include/openbabel-2.0/openbabel/data.h
/usr/include/openbabel-2.0/openbabel/data_utilities.h
/usr/include/openbabel-2.0/openbabel/descriptor.h
/usr/include/openbabel-2.0/openbabel/distgeom.h
/usr/include/openbabel-2.0/openbabel/dlhandler.h
/usr/include/openbabel-2.0/openbabel/fingerprint.h
/usr/include/openbabel-2.0/openbabel/forcefield.h
/usr/include/openbabel-2.0/openbabel/format.h
/usr/include/openbabel-2.0/openbabel/generic.h
/usr/include/openbabel-2.0/openbabel/graphsym.h
/usr/include/openbabel-2.0/openbabel/grid.h
/usr/include/openbabel-2.0/openbabel/griddata.h
/usr/include/openbabel-2.0/openbabel/groupcontrib.h
/usr/include/openbabel-2.0/openbabel/inchiformat.h
/usr/include/openbabel-2.0/openbabel/internalcoord.h
/usr/include/openbabel-2.0/openbabel/isomorphism.h
/usr/include/openbabel-2.0/openbabel/json/customwriter.h
/usr/include/openbabel-2.0/openbabel/json/json-forwards.h
/usr/include/openbabel-2.0/openbabel/json/json.h
/usr/include/openbabel-2.0/openbabel/kinetics.h
/usr/include/openbabel-2.0/openbabel/lineend.h
/usr/include/openbabel-2.0/openbabel/locale.h
/usr/include/openbabel-2.0/openbabel/math/align.h
/usr/include/openbabel-2.0/openbabel/math/erf.h
/usr/include/openbabel-2.0/openbabel/math/matrix3x3.h
/usr/include/openbabel-2.0/openbabel/math/spacegroup.h
/usr/include/openbabel-2.0/openbabel/math/transform3d.h
/usr/include/openbabel-2.0/openbabel/math/vector3.h
/usr/include/openbabel-2.0/openbabel/matrix.h
/usr/include/openbabel-2.0/openbabel/mcdlutil.h
/usr/include/openbabel-2.0/openbabel/mol.h
/usr/include/openbabel-2.0/openbabel/molchrg.h
/usr/include/openbabel-2.0/openbabel/obconversion.h
/usr/include/openbabel-2.0/openbabel/oberror.h
/usr/include/openbabel-2.0/openbabel/obiter.h
/usr/include/openbabel-2.0/openbabel/obmolecformat.h
/usr/include/openbabel-2.0/openbabel/obutil.h
/usr/include/openbabel-2.0/openbabel/op.h
/usr/include/openbabel-2.0/openbabel/optransform.h
/usr/include/openbabel-2.0/openbabel/parsmart.h
/usr/include/openbabel-2.0/openbabel/patty.h
/usr/include/openbabel-2.0/openbabel/phmodel.h
/usr/include/openbabel-2.0/openbabel/plugin.h
/usr/include/openbabel-2.0/openbabel/pointgroup.h
/usr/include/openbabel-2.0/openbabel/query.h
/usr/include/openbabel-2.0/openbabel/rand.h
/usr/include/openbabel-2.0/openbabel/reaction.h
/usr/include/openbabel-2.0/openbabel/residue.h
/usr/include/openbabel-2.0/openbabel/ring.h
/usr/include/openbabel-2.0/openbabel/rotamer.h
/usr/include/openbabel-2.0/openbabel/rotor.h
/usr/include/openbabel-2.0/openbabel/shared_ptr.h
/usr/include/openbabel-2.0/openbabel/spectrophore.h
/usr/include/openbabel-2.0/openbabel/stereo/bindings.h
/usr/include/openbabel-2.0/openbabel/stereo/cistrans.h
/usr/include/openbabel-2.0/openbabel/stereo/squareplanar.h
/usr/include/openbabel-2.0/openbabel/stereo/stereo.h
/usr/include/openbabel-2.0/openbabel/stereo/tetrahedral.h
/usr/include/openbabel-2.0/openbabel/stereo/tetranonplanar.h
/usr/include/openbabel-2.0/openbabel/stereo/tetraplanar.h
/usr/include/openbabel-2.0/openbabel/tautomer.h
/usr/include/openbabel-2.0/openbabel/text.h
/usr/include/openbabel-2.0/openbabel/tokenst.h
/usr/include/openbabel-2.0/openbabel/typer.h
/usr/include/openbabel-2.0/openbabel/xml.h
/usr/lib64/libinchi.so
/usr/lib64/libopenbabel.so
/usr/lib64/pkgconfig/openbabel-2.0.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libinchi.so.0
/usr/lib64/libinchi.so.0.4.1
/usr/lib64/libopenbabel.so.5
/usr/lib64/libopenbabel.so.5.0.0
/usr/lib64/openbabel/2.4.1/APIInterface.so
/usr/lib64/openbabel/2.4.1/CSRformat.so
/usr/lib64/openbabel/2.4.1/MCDLformat.so
/usr/lib64/openbabel/2.4.1/MNAformat.so
/usr/lib64/openbabel/2.4.1/PQSformat.so
/usr/lib64/openbabel/2.4.1/abinitformat.so
/usr/lib64/openbabel/2.4.1/acesformat.so
/usr/lib64/openbabel/2.4.1/acrformat.so
/usr/lib64/openbabel/2.4.1/adfformat.so
/usr/lib64/openbabel/2.4.1/alchemyformat.so
/usr/lib64/openbabel/2.4.1/amberformat.so
/usr/lib64/openbabel/2.4.1/aoforceformat.so
/usr/lib64/openbabel/2.4.1/asciiformat.so
/usr/lib64/openbabel/2.4.1/balstformat.so
/usr/lib64/openbabel/2.4.1/bgfformat.so
/usr/lib64/openbabel/2.4.1/boxformat.so
/usr/lib64/openbabel/2.4.1/cacaoformat.so
/usr/lib64/openbabel/2.4.1/cacheformat.so
/usr/lib64/openbabel/2.4.1/carformat.so
/usr/lib64/openbabel/2.4.1/castepformat.so
/usr/lib64/openbabel/2.4.1/cccformat.so
/usr/lib64/openbabel/2.4.1/cdxmlformat.so
/usr/lib64/openbabel/2.4.1/chem3dformat.so
/usr/lib64/openbabel/2.4.1/chemdoodlejsonformat.so
/usr/lib64/openbabel/2.4.1/chemdrawcdx.so
/usr/lib64/openbabel/2.4.1/chemdrawct.so
/usr/lib64/openbabel/2.4.1/chemkinformat.so
/usr/lib64/openbabel/2.4.1/chemtoolformat.so
/usr/lib64/openbabel/2.4.1/cifformat.so
/usr/lib64/openbabel/2.4.1/cmlformat.so
/usr/lib64/openbabel/2.4.1/cmlreactformat.so
/usr/lib64/openbabel/2.4.1/confabreport.so
/usr/lib64/openbabel/2.4.1/copyformat.so
/usr/lib64/openbabel/2.4.1/crkformat.so
/usr/lib64/openbabel/2.4.1/crystal09format.so
/usr/lib64/openbabel/2.4.1/cssrformat.so
/usr/lib64/openbabel/2.4.1/daltonformat.so
/usr/lib64/openbabel/2.4.1/dlpolyformat.so
/usr/lib64/openbabel/2.4.1/dmolformat.so
/usr/lib64/openbabel/2.4.1/exyzformat.so
/usr/lib64/openbabel/2.4.1/fastaformat.so
/usr/lib64/openbabel/2.4.1/fastsearchformat.so
/usr/lib64/openbabel/2.4.1/fchkformat.so
/usr/lib64/openbabel/2.4.1/featformat.so
/usr/lib64/openbabel/2.4.1/fhformat.so
/usr/lib64/openbabel/2.4.1/fhiaimsformat.so
/usr/lib64/openbabel/2.4.1/fingerprintformat.so
/usr/lib64/openbabel/2.4.1/fpsformat.so
/usr/lib64/openbabel/2.4.1/freefracformat.so
/usr/lib64/openbabel/2.4.1/gamessformat.so
/usr/lib64/openbabel/2.4.1/gamessukformat.so
/usr/lib64/openbabel/2.4.1/gausscubeformat.so
/usr/lib64/openbabel/2.4.1/gaussformat.so
/usr/lib64/openbabel/2.4.1/gausszmatformat.so
/usr/lib64/openbabel/2.4.1/ghemicalformat.so
/usr/lib64/openbabel/2.4.1/groformat.so
/usr/lib64/openbabel/2.4.1/gromos96format.so
/usr/lib64/openbabel/2.4.1/gulpformat.so
/usr/lib64/openbabel/2.4.1/hinformat.so
/usr/lib64/openbabel/2.4.1/inchiformat.so
/usr/lib64/openbabel/2.4.1/jaguarformat.so
/usr/lib64/openbabel/2.4.1/lmpdatformat.so
/usr/lib64/openbabel/2.4.1/lpmdformat.so
/usr/lib64/openbabel/2.4.1/mdffformat.so
/usr/lib64/openbabel/2.4.1/mdlformat.so
/usr/lib64/openbabel/2.4.1/mmcifformat.so
/usr/lib64/openbabel/2.4.1/mmodformat.so
/usr/lib64/openbabel/2.4.1/mol2format.so
/usr/lib64/openbabel/2.4.1/moldenformat.so
/usr/lib64/openbabel/2.4.1/molproformat.so
/usr/lib64/openbabel/2.4.1/molreport.so
/usr/lib64/openbabel/2.4.1/mopacformat.so
/usr/lib64/openbabel/2.4.1/mpdformat.so
/usr/lib64/openbabel/2.4.1/mpqcformat.so
/usr/lib64/openbabel/2.4.1/msiformat.so
/usr/lib64/openbabel/2.4.1/msmsformat.so
/usr/lib64/openbabel/2.4.1/nulformat.so
/usr/lib64/openbabel/2.4.1/nwchemformat.so
/usr/lib64/openbabel/2.4.1/opendxformat.so
/usr/lib64/openbabel/2.4.1/orcaformat.so
/usr/lib64/openbabel/2.4.1/outformat.so
/usr/lib64/openbabel/2.4.1/painterformat.so
/usr/lib64/openbabel/2.4.1/pcmodelformat.so
/usr/lib64/openbabel/2.4.1/pdbformat.so
/usr/lib64/openbabel/2.4.1/pdbqtformat.so
/usr/lib64/openbabel/2.4.1/plugin_charges.so
/usr/lib64/openbabel/2.4.1/plugin_descriptors.so
/usr/lib64/openbabel/2.4.1/plugin_fingerprints.so
/usr/lib64/openbabel/2.4.1/plugin_forcefields.so
/usr/lib64/openbabel/2.4.1/plugin_ops.so
/usr/lib64/openbabel/2.4.1/png2format.so
/usr/lib64/openbabel/2.4.1/pngformat.so
/usr/lib64/openbabel/2.4.1/pointcloudformat.so
/usr/lib64/openbabel/2.4.1/posformat.so
/usr/lib64/openbabel/2.4.1/povrayformat.so
/usr/lib64/openbabel/2.4.1/pqrformat.so
/usr/lib64/openbabel/2.4.1/pubchem.so
/usr/lib64/openbabel/2.4.1/pubchemjsonformat.so
/usr/lib64/openbabel/2.4.1/pwscfformat.so
/usr/lib64/openbabel/2.4.1/qchemformat.so
/usr/lib64/openbabel/2.4.1/reportformat.so
/usr/lib64/openbabel/2.4.1/rsmiformat.so
/usr/lib64/openbabel/2.4.1/rxnformat.so
/usr/lib64/openbabel/2.4.1/shelxformat.so
/usr/lib64/openbabel/2.4.1/siestaformat.so
/usr/lib64/openbabel/2.4.1/smilesformat.so
/usr/lib64/openbabel/2.4.1/smileyformat.so
/usr/lib64/openbabel/2.4.1/stlformat.so
/usr/lib64/openbabel/2.4.1/svgformat.so
/usr/lib64/openbabel/2.4.1/textformat.so
/usr/lib64/openbabel/2.4.1/thermoformat.so
/usr/lib64/openbabel/2.4.1/tinkerformat.so
/usr/lib64/openbabel/2.4.1/titleformat.so
/usr/lib64/openbabel/2.4.1/turbomoleformat.so
/usr/lib64/openbabel/2.4.1/unichemformat.so
/usr/lib64/openbabel/2.4.1/vaspformat.so
/usr/lib64/openbabel/2.4.1/viewmolformat.so
/usr/lib64/openbabel/2.4.1/xedformat.so
/usr/lib64/openbabel/2.4.1/xmlformat.so
/usr/lib64/openbabel/2.4.1/xsfformat.so
/usr/lib64/openbabel/2.4.1/xtcformat.so
/usr/lib64/openbabel/2.4.1/xyzformat.so
/usr/lib64/openbabel/2.4.1/yasaraformat.so
/usr/lib64/openbabel/2.4.1/zindoformat.so
