//Maya ASCII 2016 scene
//Name: Face_ForeHead_Plane.ma
//Last modified: Fri, Aug 26, 2016 02:31:17 PM
//Codeset: 936
requires maya "2016";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201603180400-990260";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "ForeHead_GRP";
	rename -uid "11DD3030-4D98-D358-D46D-0B8943DE1712";
	setAttr ".rp" -type "double3" 0 12.463955856693198 11.047644938118729 ;
	setAttr ".sp" -type "double3" 0 12.463955856693198 11.047644938118729 ;
createNode transform -n "ForeHead_Plane" -p "ForeHead_GRP";
	rename -uid "E158B456-4406-E232-5590-28BFCAB22532";
	setAttr ".t" -type "double3" 0 12.463955856693198 11.047644938118729 ;
	setAttr ".r" -type "double3" 72.83649259468622 0 0 ;
	setAttr ".s" -type "double3" 5.3787294190973451 5.3787294190973451 5.3787294190973451 ;
createNode mesh -n "ForeHead_PlaneShape" -p "ForeHead_Plane";
	rename -uid "116A05BC-4FEC-E274-3F77-CCA627767194";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 9 ".uvst[0].uvsp[0:8]" -type "float2" 0 0 0.5 0 1 0 0 0.5
		 0.5 0.5 1 0.5 0 1 0.5 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 9 ".pt[0:8]" -type "float3"  -0.24500151 0 -5.9952043e-015 
		0 0 -5.9952043e-015 0.24500151 0 -5.9952043e-015 -0.24500151 0 -5.9952043e-015 0 
		0 -5.9952043e-015 0.24500151 0 -5.9952043e-015 -0.24500151 0 -5.9952043e-015 0 0 
		-5.9952043e-015 0.24500151 0 -5.9952043e-015;
	setAttr -s 9 ".vt[0:8]"  -0.5 -1.110223e-016 0.5 0 -1.110223e-016 0.5
		 0.5 -1.110223e-016 0.5 -0.5 0 0 0 0 0 0.5 0 0 -0.5 1.110223e-016 -0.5 0 1.110223e-016 -0.5
		 0.5 1.110223e-016 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 0 3 0 1 2 0 1 4 1 2 5 0 3 4 1 3 6 0
		 4 5 1 4 7 1 5 8 0 6 7 0 7 8 0;
	setAttr -s 4 -ch 16 ".fc[0:3]" -type "polyFaces" 
		f 4 0 3 -6 -2
		mu 0 4 0 1 4 3
		f 4 2 4 -8 -4
		mu 0 4 1 2 5 4
		f 4 5 8 -11 -7
		mu 0 4 3 4 7 6
		f 4 7 9 -12 -9
		mu 0 4 4 5 8 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "ForeHead_follicleGroup" -p "ForeHead_GRP";
	rename -uid "11797E9D-4BDF-B0BA-3A38-08B5ECD6CFA4";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode transform -n "ForeHead_R_follicle" -p "ForeHead_follicleGroup";
	rename -uid "D692BB2D-4CBC-7598-EA92-E397F8FF6DA9";
createNode follicle -n "ForeHead_R_follicleShape" -p "ForeHead_R_follicle";
	rename -uid "D2AB2020-4E60-ED73-0BC9-8EA3FD28171D";
	setAttr -k off ".v";
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode joint -n "ForeHead_R" -p "ForeHead_R_follicle";
	rename -uid "104721D7-4412-9342-460F-7A8CC4F56817";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 17.163507405313766 -2.0706278133148108e-015 -180 ;
	setAttr ".sd" 3;
	setAttr ".radi" 0.5;
createNode transform -n "ForeHead_L_follicle" -p "ForeHead_follicleGroup";
	rename -uid "7FB72076-4DCD-3996-86D2-2FA8814326BD";
createNode follicle -n "ForeHead_L_follicleShape" -p "ForeHead_L_follicle";
	rename -uid "49E08C54-41C3-8484-DE76-338917486057";
	setAttr -k off ".v";
	setAttr ".pu" 1;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode joint -n "ForeHead_L" -p "ForeHead_L_follicle";
	rename -uid "77F56CAD-4DAB-7D07-8459-A5A76728A2BC";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 17.163507405313766 -2.0706278133148108e-015 -180 ;
	setAttr ".otp" -type "string" "xxx";
	setAttr ".radi" 0.5;
createNode transform -n "ForeHead_M_follicle" -p "ForeHead_follicleGroup";
	rename -uid "8D785CA0-4CD8-A7D1-BBA5-DF9EDEF69879";
createNode follicle -n "ForeHead_M_follicleShape" -p "ForeHead_M_follicle";
	rename -uid "6DD3723C-4B6C-EC59-5CDB-11A8418C0178";
	setAttr -k off ".v";
	setAttr ".pu" 0.5;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode joint -n "ForeHead_M" -p "ForeHead_M_follicle";
	rename -uid "29E530EF-44FC-4F5B-C4CD-8D8DF0FEC1D7";
	addAttr -ci true -k true -sn "twistJoints" -ln "twistJoints" -dv 2 -min 0 -max 
		10 -at "long";
	addAttr -ci true -k true -sn "bendyJoints" -ln "bendyJoints" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 17.163507405313766 -2.0706278133148108e-015 -180 ;
	setAttr ".otp" -type "string" "d";
	setAttr ".radi" 0.5;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 3 ".st";
	setAttr -k on ".an";
	setAttr -k on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :lambert1;
	setAttr ".c" -type "float3" 0.85000002 0.85000002 0.85000002 ;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 11 ".dsm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
	setAttr -s 2 ".gn";
select -ne :initialParticleSE;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off ".eeaa";
	setAttr -k off ".engm";
	setAttr -k off ".mes";
	setAttr -k off ".emb";
	setAttr -k off ".mbbf";
	setAttr -k off ".mbs";
	setAttr -k off ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off ".twa";
	setAttr -k off ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "ForeHead_R_follicleShape.ot" "ForeHead_R_follicle.t";
connectAttr "ForeHead_R_follicleShape.or" "ForeHead_R_follicle.r";
connectAttr "ForeHead_PlaneShape.o" "ForeHead_R_follicleShape.inm";
connectAttr "ForeHead_PlaneShape.wm" "ForeHead_R_follicleShape.iwm";
connectAttr "ForeHead_L_follicleShape.ot" "ForeHead_L_follicle.t";
connectAttr "ForeHead_L_follicleShape.or" "ForeHead_L_follicle.r";
connectAttr "ForeHead_PlaneShape.o" "ForeHead_L_follicleShape.inm";
connectAttr "ForeHead_PlaneShape.wm" "ForeHead_L_follicleShape.iwm";
connectAttr "ForeHead_M_follicleShape.ot" "ForeHead_M_follicle.t";
connectAttr "ForeHead_M_follicleShape.or" "ForeHead_M_follicle.r";
connectAttr "ForeHead_PlaneShape.o" "ForeHead_M_follicleShape.inm";
connectAttr "ForeHead_PlaneShape.wm" "ForeHead_M_follicleShape.iwm";
connectAttr "ForeHead_PlaneShape.iog" ":initialShadingGroup.dsm" -na;
// End of Face_ForeHead_Plane.ma
