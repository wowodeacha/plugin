//Maya ASCII 2014 scene
//Name: Face_Base_Loc.ma
//Last modified: Tue, Jun 14, 2016 10:53:18 AM
//Codeset: 936
requires maya "2014";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2014";
fileInfo "version" "2014 x64";
fileInfo "cutIdentifier" "201303010241-864206";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "_testChar_HeadLoc";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "_testChar_HeadLocShape" -p "_testChar_HeadLoc";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
createNode transform -n "_testChar_HeadEndLoc" -p "_testChar_HeadLoc";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 0 3.3 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "_testChar_HeadEndLocShape" -p "_testChar_HeadEndLoc";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
createNode nurbsSurface -n "_testChar_HeadEndLocShape1" -p "_testChar_HeadEndLoc";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".cc" -type "nurbsSurface" 
		3 3 0 0 no 
		6 0 0 0 1 1 1
		6 0 0 0 1 1 1
		
		16
		-3 -1.8369701987210294e-016 3
		-3 -6.1232339957367673e-017 1
		-3 6.1232339957367648e-017 -0.99999999999999978
		-3 1.8369701987210294e-016 -3
		-1 -1.8369701987210294e-016 3
		-1 -6.1232339957367673e-017 1
		-1 6.1232339957367648e-017 -0.99999999999999978
		-1 1.8369701987210294e-016 -3
		0.99999999999999978 -1.8369701987210294e-016 3
		0.99999999999999978 -6.1232339957367673e-017 1
		0.99999999999999978 6.1232339957367648e-017 -0.99999999999999978
		0.99999999999999978 1.8369701987210294e-016 -3
		3 -1.8369701987210294e-016 3
		3 -6.1232339957367673e-017 1
		3 6.1232339957367648e-017 -0.99999999999999978
		3 1.8369701987210294e-016 -3
		
		;
	setAttr ".nufa" 4.5;
	setAttr ".nvfa" 4.5;
createNode transform -n "Head_Scale_curve" -p "_testChar_HeadLoc";
	addAttr -ci true -sn "orgLength" -ln "orgLength" -at "double";
	setAttr -l on ".v";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".it" no;
	setAttr -l on -k on ".orgLength" 3.3;
createNode nurbsCurve -n "Head_Scale_curveShape" -p "Head_Scale_curve";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr -s 2 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		0 3.2999999999999998 0
		;
createNode nurbsSurface -n "_testChar_HeadLocShape1" -p "_testChar_HeadLoc";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".cc" -type "nurbsSurface" 
		3 3 0 0 no 
		6 0 0 0 1 1 1
		6 0 0 0 1 1 1
		
		16
		-3 -1.8369701987210297e-016 3
		-3 -6.1232339957367673e-017 1
		-3 6.1232339957367648e-017 -0.99999999999999978
		-3 1.8369701987210297e-016 -3
		-1 -1.8369701987210297e-016 3
		-1 -6.1232339957367673e-017 1
		-1 6.1232339957367648e-017 -0.99999999999999978
		-1 1.8369701987210297e-016 -3
		0.99999999999999978 -1.8369701987210297e-016 3
		0.99999999999999978 -6.1232339957367673e-017 1
		0.99999999999999978 6.1232339957367648e-017 -0.99999999999999978
		0.99999999999999978 1.8369701987210297e-016 -3
		3 -1.8369701987210297e-016 3
		3 -6.1232339957367673e-017 1
		3 6.1232339957367648e-017 -0.99999999999999978
		3 1.8369701987210297e-016 -3
		
		;
	setAttr ".nufa" 4.5;
	setAttr ".nvfa" 4.5;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -s 7 ".st";
select -ne :initialShadingGroup;
	setAttr -s 5 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 7 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -s 2 ".r";
select -ne :renderGlobalsList1;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 18 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surfaces" "Particles" "Fluids" "Image Planes" "UI:" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 18 0 1 1 1 1 1
		 1 0 0 0 0 0 0 0 0 0 0 0 ;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "_testChar_HeadLocShape.wp" "Head_Scale_curveShape.cp[0]";
connectAttr "_testChar_HeadEndLocShape.wp" "Head_Scale_curveShape.cp[1]";
// End of Face_Base_Loc.ma
