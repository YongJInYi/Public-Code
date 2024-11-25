import maya.cmds as cmds

#############################################################################################################
world = [[0, 0, -11.961027], [0.901469, 0, -10.574109], [0.535792, 0, 0.341248], [1.545726, 0, 3.556168], 
            [0, 0, 5.964304], [-1.545726, 0, 3.556168], [-0.535792, 0, 0.341248], [-0.901469, 0, -10.574109], [0, 0, -11.961027]]

Pin2x = [[0, 0.536726, 0], [0.0836721, 0.509539, 0], [0.135384, 0.438363, 0], [0.135384, 0.350385, 0], [0.0836721, 0.27921, 0], 
            [0, 0.252023, 0], [0, 0.00108498, 0], [0, -0.402187, 0], [0.0845694, -0.429666, 0], [0.136836, -0.501605, 0], [0.136836, -0.590526, 0], 
                [0.0845694, -0.662465, 0], [0, -0.689943, 0], [-0.0845694, -0.662465, 0], [-0.136836, -0.590526, 0], [-0.136836, -0.501605, 0], [-0.0845694, -0.429666, 0], 
                    [0, -0.402187, 0], [0, 0.00108498, 0], [0, 0.252023, 0], [-0.083672, 0.27921, 0], [-0.135384, 0.350385, 0], [-0.135384, 0.438363, 0], [-0.083672, 0.509539, 0], [0, 0.536726, 0]]

snakehead = [[1, 0, -0.325], [1, 0, 0.325], [1, -0.284339, 0.325], [1, -0.284339, -0.325], [1, 0, -0.325], 
                [0.218202, 0.275911, -0.5], [-0.25, 0.275911, -0.5], [-0.25, 0.275911, 0.5], [0.218202, 0.275911, 0.5], 
                    [0.218202, 0.275911, -0.5], [0.218202, -0.284339, -0.5], [0.218202, -0.284339, 0.5], [-0.25, -0.284339, 0.5], 
                        [-0.25, -0.284339, -0.5], [0.218202, -0.284339, -0.5], [1, -0.284339, -0.325], [1, -0.284339, 0.325], [0.218202, -0.284339, 0.5],
                            [-0.25, -0.284339, 0.5], [-0.25, 0.275911, 0.5], [0.218202, 0.275911, 0.5], [1, 0, 0.325], [0.218202, 0.275911, 0.5], [0.218202, -0.284339, 0.5], 
                                [0.218202, -0.284339, -0.5], [-0.25, -0.284339, -0.5], [-0.25, 0.275911, -0.5]]

cube = [[-0.09, 0.45, -0.45], [0.09, 0.45, -0.45], [0.09, 0.45, 0.45], [-0.09, 0.45, 0.45], 
            [-0.09, 0.45, -0.45], [-0.09, -0.45, -0.45], [0.09, -0.45, -0.45], [0.09, 0.45, -0.45], 
                [0.09, 0.45, 0.45], [0.09, -0.45, 0.45], [0.09, -0.45, -0.45], [-0.09, -0.45, -0.45], 
                    [-0.09, -0.45, 0.45], [0.09, -0.45, 0.45], [0.09, 0.45, 0.45], [-0.09, 0.45, 0.45], 
                        [-0.09, -0.45,0.45]]

circle = [[0, 0.427006, 0], [0, 0.394502, -0.163408], [0, 0.301939, -0.301939], [0, 0.163408, -0.394502], 
            [0, 0, -0.427006], [0, -0.163408, -0.394502], [0, -0.301939, -0.301939], [0, -0.394502, -0.163408], 
                [0, -0.427006, 0], [0, -0.394502, 0.163408], [0, -0.301939, 0.301939], [0, -0.163408, 0.394502], 
                    [0, 0, 0.427006], [0, 0.163408, 0.394502], [0, 0.301939, 0.301939], [0, 0.394502, 0.163408], 
                        [0, 0.427006, 0]]

offset = [[1.603937, 3.074125, 0], [2.222387, 3.074125, 0], [2.75798, 2.7649, 0], [3.067204, 2.229307, 0], 
            [3.067204, 1.610858, 0], [3.067204, -1.559976, 0], [3.067204, -2.178425, 0], [2.75798, -2.714018, 0], 
                [2.222387, -3.023242, 0], [-2.185346, -3.023242, 0], [-2.720939, -2.714018, 0], [-3.030163, -2.178425, 0], 
                    [-3.030163, 2.229307, 0], [-2.720939, 2.7649, 0 ], [-2.185346, 3.074125, 0], [-1.566896, 3.074125, 0], 
                        [1.603937, 3.074125, 0]]

Pyramid = [[0.853754, 0, 0], [0.178618, 0.337568, -0.337568], [0.178618, -0.337568, -0.337568], [0.853754, 0, 0], 
            [0.178618, 0.337568, 0.337568], [0.178618, -0.337568, 0.337568], [0.853754, 0, 0], [0.178618, -0.337568, -0.337568], 
                [0.178618, -0.337568, 0.337568], [0.178618, 0.337568, 0.337568], [0.178618, 0.337568, -0.337568]]

Arrow2Way = [[1.00187, 0, 0], [0.500935, 0.500935, 0], [0.500935, 0.250468, 0], [-0.500935, 0.250468, 0], 
                [-0.500935, 0.500935, 0], [-1.00187, 0, 0], [-0.500935, -0.500935, 0], [-0.500935, -0.250468, 0], 
                    [0.500935, -0.250468, 0], [0.500935, -0.500935, 0], [1.00187, 0, 0]]


class snake():
    #############################################################################################################
    def tool_ui(self):
        if cmds.window('snake_tool', exists=True):
                    cmds.deleteUI('snake_tool')

        width = 400
        Height = 185
        window = cmds.window('snake_tool', title="Snake Tool", iconName='Snake Tool', widthHeight=(width, Height) )

        cmds.columnLayout( adjustableColumn=True )

        cmds.rowColumnLayout(numberOfRows=1) #1
        cmds.text(label='aspect: ' )
        cmds.textField('aspect', text='m', w=width / 3.4)
        cmds.text(label=' Name: ' )
        cmds.textField('name', text='Snake', w=width / 3.4)
        cmds.button(label='Create Locate ', command=self.create_locate)
        cmds.setParent( '..' ) #1
        cmds.separator(height=1)

        cmds.frameLayout('create_interface', label='Create Interface', cll=False, collapse=False, w=width, enable=False)# Create Joint Locate
        cmds.rowColumnLayout(numberOfRows=2) #2

        cmds.intSliderGrp('headNumber', l='Head Bone', field=True, value=4, dragCommand=self.head_interaction_Increased_bone, enable=True)
        cmds.popupMenu()
        cmds.menuItem('menuItem_headNumber', label='Refresh', command=self.head_interaction_Increased_bone)

        cmds.intSliderGrp('tailNumber', l='Tail Bone', field=True, value=13, dragCommand=self.tail_interaction_Increased_bone, enable=True)
        cmds.popupMenu()
        cmds.menuItem('menuItem_tailNumber', label='Refresh', command=self.tail_interaction_Increased_bone)

        cmds.setParent( '..' ) #2

        # Create bones directly without manually adjusting them
        cmds.checkBox('manual_adjustment', label='Manual Adjustment', value=True, cc='None')
        cmds.button('createJoint', label='Create Joint', command=self.Manual_Adjustment_Create_Joint, enable=True)
        
        # Right click to create bones after manual adjustments
        cmds.popupMenu()
        cmds.menuItem('manual_adjustment_create_joint', label='Manual Adjustment Create Joint', command=self.adjust_create_joint)

        cmds.button('Run', label='Run', command=self.run, enable=True)

        cmds.setParent( '..' )# Create Joint Locate

        cmds.setParent( '..' )
        cmds.showWindow( window )
        cmds.window('snake_tool', e=True, wh=[width, Height])
    
    def createCurve(self, obj, dr=1, name='',):
        """
        obj(list) : Selecting an object can calculate the position and create a curve 
        """
        
        obj = obj
        
        point = []
        knot = []
        for i in enumerate(obj):
            translation = cmds.xform(i[1], query=True, translation=True, worldSpace=True)
            knot.append(i[0])
            point.append(translation)
        
        head = obj[0].split('_')
        # create curve
        curve = cmds.curve(degree=int(dr), point=point, name=self.name)
        # rename curve
        cmds.rename(cmds.listRelatives(curve, shapes=True), curve + 'Shape')
        return curve

    def bisection_value(self, number):
        number_lit = []
        UValue = 1.0 / number
        for head in range(number + 1):
            get_UValue = UValue * (head)
            number_lit.append(get_UValue)
        
        return number_lit

    def Hierarchical_group(self, ctrl): 
        # get selected nurbs curve as controller
        ctrls = [ctrl]
        zero_lit = []
        output_lit = []
        if ctrls:
            # loop in each ctrl and create hierarchy
            for ctrl in ctrls:
                # get name parts
                name_parts = ctrl.split('_')
                if len(name_parts) == 4:
                    zero_name = ctrl.replace(name_parts[0] + '_', 'zero_')
                    driven_name = ctrl.replace(name_parts[0] + '_', 'driven_')
                    space_name = ctrl.replace(name_parts[0] + '_', 'space_')
                    connect_name = ctrl.replace(name_parts[0] + '_', 'connect_')
                    offset_name = ctrl.replace(name_parts[0] + '_', 'offset_')
                    
                elif len(name_parts) < 4:
                    zero_name = 'zero_{0}'.format(name_parts[0])
                    driven_name = 'driven_{0}'.format(name_parts[0])
                    space_name = 'space_{0}'.format(name_parts[0])
                    connect_name = 'connect_{0}'.format(name_parts[0])
                    offset_name = 'offset_{0}'.format(name_parts[0])
                    
                # create zero group
                zero = cmds.createNode('transform', name=zero_name)
                # create driven group
                driven = cmds.createNode('transform', name=driven_name, parent=zero)
                # create space group
                space = cmds.createNode('transform', name=space_name, parent=driven)
                # create connect group
                connect = cmds.createNode('transform', name=connect_name, parent=space)
                # create offset group
                offset = cmds.createNode('transform', name=offset_name, parent=connect)
                
                # snap to control position
                cmds.matchTransform(zero, ctrl, position=True, rotation=True)
                
                # zero scale numerical value
                cmds.makeIdentity(ctrl, apply=True, scale=True)
                
                # parent control to offset group
                cmds.parent(ctrl, offset)
                
                zero_lit.append(zero)
                
        return zero_lit

    # curve create nurbsSurface
    def nurbsSurface(self, curve_one, curve_two, surface_name):

        """
        curve_one(str): First curve
        curve_two(str): Second Curve
        surface_name(str): nurbsSurface the name
        """
        
        # get curve one and curve two shapes 
        curve_one_shape = cmds.listRelatives(curve_one, shapes=True)[0]
        curve_two_shape = cmds.listRelatives(curve_two, shapes=True)[0]
        
        # create loft node 
        loft = cmds.createNode('loft', name='loft_' + self.aspect + '_' + self.name + 'createDel_001')
        # create nurbsSurface
        nurbsSurface = cmds.createNode('nurbsSurface', name=surface_name + 'Shape')

        # connect node 
        cmds.connectAttr(curve_one_shape + '.worldSpace[0]', loft + '.inputCurve[0]')
        cmds.connectAttr(curve_two_shape + '.worldSpace[0]', loft + '.inputCurve[1]')
        cmds.connectAttr(loft + '.outputSurface', nurbsSurface + '.create')

        # set Maps
        cmds.sets(surface_name, edit=True, forceElement='initialShadingGroup')
        
        # DeleteHistory
        cmds.DeleteHistory(surface_name)
        
    # create foll the connect 
    def create_foll_setUV(self, tail, surface_shape, ParameterU, ParameterV, foll_name):
        """
        tail(int): foll name tail
        surface_shape(str): get uv the surface shape
        ParameterU(int): set foll shapes ParameterU
        ParameterV(int): set foll shapes ParameterV
        foll_name(str): set foll name 
        """
        foll_name = 'foll_' + self.aspect + '_' + self.name + foll_name + '_{:03d}'.format(tail)
        foll_shape = cmds.createNode('follicle', name=foll_name + 'Shape')

        # connect 
        cmds.connectAttr(foll_shape + '.outTranslate', foll_name + '.translate')
        cmds.connectAttr(foll_shape + '.outRotate', foll_name + '.rotate')

        cmds.connectAttr(surface_shape + '.inverseMatrix', foll_shape + '.inputWorldMatrix')
        cmds.connectAttr(surface_shape + '.worldSpace[0]', foll_shape + '.inputSurface')

        # set parameter UV 
        cmds.setAttr(foll_shape + '.parameterU', ParameterU)
        cmds.setAttr(foll_shape + '.parameterV', ParameterV)
        
        return foll_name

    def get_UV(self, surface_shape, jnt_name):
        # get surface ParameterU ParameterV
        """
        surface_shape(str): get uv the surface shape
        jnt_name(str): bone get translate 
        
        
        """
        # create node 
        closestPointOnSurface = cmds.createNode('closestPointOnSurface', 
                                                    name='closest_' + self.aspect + '_' + self.name + 'closestPointOnSurfaceDel_001')

        # create locator
        locator_shape = cmds.createNode('locator', name='loc_' + self.aspect + '_' + self.name + 'locatorDel_001Shape')
        locator_transform = cmds.listRelatives(locator_shape, parent=True)[0]

        # set loc translate 
        cmds.delete(cmds.pointConstraint(jnt_name, locator_transform))

        # connect 
        cmds.connectAttr(surface_shape + '.worldSpace[0]', closestPointOnSurface + '.inputSurface')
        cmds.connectAttr(locator_shape + '.worldPosition[0]', closestPointOnSurface + '.inPosition')

        # get  ParameterU ParameterV
        ParameterU = cmds.getAttr(closestPointOnSurface + '.parameterU')
        ParameterV = cmds.getAttr(closestPointOnSurface + '.parameterV')
        
        cmds.delete(locator_transform)
        
        return [ParameterU, ParameterV]

    def trntacleRoll(self, ctrl, jnts, prefix):
        ###################################
        Drvname = [ctrl.split('_')[0], ctrl.split('_')[1], ctrl.split('_')[2], ctrl.split('_')[3]]

        # add attrs
        cmds.addAttr(ctrl, longName=prefix + 'Roll', attributeType='float', minValue=0, maxValue=10, keyable=True)
        cmds.addAttr(ctrl, longName=prefix + 'Angle', attributeType='float', keyable=True, defaultValue=70)
        cmds.addAttr(ctrl, longName=prefix + 'Falloff', attributeType='float', keyable=True, minValue=0, maxValue=1, defaultValue=0.1)
        cmds.addAttr(ctrl, longName=prefix + 'Orientation', attributeType='float', keyable=True, minValue=0, maxValue=1, defaultValue=1)
        
        roll_attr = ctrl + '.{}Roll'.format(prefix)
        angle_attr = ctrl + '.{}Angle'.format(prefix)
        falloff_attr = ctrl + '.{}Falloff'.format(prefix)
        orientation_attr = ctrl + '.{}Orientation'.format(prefix)
        
        # mult node to reverse falloff value, because we are using this value to subtract
        mult = cmds.createNode('multDoubleLinear', name='mult_' + Drvname[1] + '_' + Drvname[2] + '_' + Drvname[3])
        cmds.connectAttr(falloff_attr, mult + '.input1')
        cmds.setAttr(mult + '.input2', -1)
        falloff_attr = mult + '.output'

        ###################################

        # get control number
        ctrl_num = len(jnts)

        # create mash distribute node 
        distr = cmds.createNode('MASH_Distribute', name='distribute_' + Drvname[1] + '_' + Drvname[2] + prefix + 'Roll_' + Drvname[3])
        cmds.setAttr(distr + '.pointCount', ctrl_num)

        # set rotate X to 1 gather weight value from 0-1
        cmds.setAttr(distr + '.rotateX', 1)

        # create breakout node
        breakout = cmds.createNode('MASH_Breakout', name='breakout_' + Drvname[1] + '_' + Drvname[2] + 'Roll_' + Drvname[3])
        cmds.connectAttr(distr + '.outputPoints', breakout + '.inputPoints')

        # loop in each control to do the roll setup
        for i, ctrl in enumerate(jnts):
            # get connect group
            connect = ctrl.replace('ctrl_', 'space_')
            ctrlname = [ctrl.split('_')[0], ctrl.split('_')[1], ctrl.split('_')[2], ctrl.split('_')[3]]
            # create remap node to roll wuill only happen in the given section
            remap = cmds.createNode('remapValue', name='remap_' + ctrlname[1] + '_' + ctrlname[2] + 'RollWeight_' + ctrlname[3])
            
            # Create Node Reset Attribute Size
            remap_resetting = cmds.createNode('remapValue', name='remap_' + ctrlname[1] + '_' + ctrlname[2] + 'ResettingRollWeight_' + ctrlname[3])

            # connect tentacle roll to remap 
            cmds.connectAttr(roll_attr, remap_resetting + '.inputValue')
            cmds.connectAttr(remap_resetting + '.outValue', remap + '.inputValue')
            
            # set resetting remap inputMax
            cmds.setAttr(remap_resetting + '.inputMax', 10)
            
            # get max value by weight
            weight_max = 1 - float(i) / ctrl_num
            cmds.setAttr(remap + '.inputMax', weight_max)
            # get min value
            weight_min = 1 - float(i+1)/ctrl_num
            # add node to subtract falloff so the joint can roll before the previous finished 
            add = cmds.createNode('addDoubleLinear', name='add_' + ctrlname[1] + '_' + ctrlname[2] + 'RollStart_' + ctrlname[3])
            cmds.setAttr(add + '.input1', weight_min)
            cmds.connectAttr(falloff_attr, add + '.input2')
            # clamp value so it won't go below 0
            clamp = cmds.createNode('clamp', name='clamp_' + ctrlname[1] + '_' + ctrlname[2] + 'RollStart_' + ctrlname[3])
            cmds.setAttr(clamp + '.maxR', 1)
            cmds.connectAttr(add + '.output', clamp + '.inputR')
            # connect with min value 
            cmds.connectAttr(clamp + '.outputR', remap + '.inputMin')
            
            # multiply divide node to mult remap weight with distribute weight to get the final roll weigt for each joint
            # because MASH doesn't work with single axis, we need to uese multiply divide to breakout single axis rotation
            mult_weight = cmds.createNode('multiplyDivide', name='mult_' + ctrlname[1] + '_' + ctrlname[2] + 'RotWeight_' + ctrlname[3])
            cmds.connectAttr(remap + '.outValue', mult_weight + '.input1X')
            cmds.connectAttr('{}.outputs[{}].rotate'.format(breakout, i), mult_weight + '.input2')
            
            # mult with roll angle to get output
            mult_angle = cmds.createNode('multDoubleLinear', name='mult_' + ctrlname[1] + '_' + ctrlname[2] + 'RotAngle_' + ctrlname[3])
            cmds.connectAttr(mult_weight + '.outputX', mult_angle + '.input1')
            cmds.connectAttr(angle_attr, mult_angle + '.input2')
            
            # create remapValue Set rotation axis
            remap_Y = cmds.createNode('remapValue', name='remap_' + ctrlname[1] + '_' + ctrlname[2] + 'RollWeightY_' + ctrlname[3])
            remap_Z = cmds.createNode('remapValue', name='remap_' + ctrlname[1] + '_' + ctrlname[2] + 'RollWeightZ_' + ctrlname[3])
            
            # set remapValue
            cmds.setAttr(remap_Y + '.inputMax', 0)
            cmds.setAttr(remap_Y + '.outputMax', 0)
            cmds.setAttr(remap_Y + '.inputMin', 1)
            
            cmds.setAttr(remap_Z + '.outputMax', 0)
            cmds.setAttr(remap_Z + '.inputMax', 0)
            cmds.setAttr(remap_Z + '.inputMin', 1)
            
            # connect rotation axis remapValue
            cmds.connectAttr(orientation_attr, remap_Y + '.inputValue')
            cmds.connectAttr(orientation_attr, remap_Z + '.inputValue')
            
            cmds.connectAttr(mult_angle + '.output', remap_Y + '.outputMin')
            cmds.connectAttr(mult_angle + '.output', remap_Z + '.outputMax')
            
            cmds.connectAttr(remap_Y + '.outValue', connect + '.rotateY')
            cmds.connectAttr(remap_Z + '.outValue', connect + '.rotateZ')
        
        return distr

    def createCurve(self, objects, name, dr=1):
        """
        objects(list) : Selecting an object can calculate the position and create a curve 
        
        """
        
        obj = objects
        
        point = []
        knot = []
        for i in enumerate(obj):
            translation = cmds.xform(i[1], query=True, translation=True, worldSpace=True)
            knot.append(i[0])
            point.append(translation)
        
        head = obj[0].split('_')
        # create curve
        curve = cmds.curve(degree=int(dr), point=point, name=name)
        # rename curve
        cmds.rename(cmds.listRelatives(curve, shapes=True), curve + 'Shape')
        return curve

    #############################################################################################################
    def head_interaction_Increased_bone(self, *args):
        self.headNumber = cmds.intSliderGrp('headNumber', query=True, value=True)
        cmds.setAttr(self.head_locator + '.boneSegments', self.headNumber)
    
    def tail_interaction_Increased_bone(self, *args):
        self.tailNumber = cmds.intSliderGrp('tailNumber', query=True, value=True)
        cmds.setAttr(self.tail_locator + '.boneSegments', self.tailNumber)
    
    def key_enable_True(self, *args):
        cmds.frameLayout('create_interface', edit=True, enable=True)
    
    def Number_enable_False(self, *args):
        # hide locator 
        cmds.setAttr(self.middle_locator + '.visibility', False)
        
        cmds.intSliderGrp('headNumber', edit=True, enable=False)
        cmds.intSliderGrp('tailNumber', edit=True, enable=False)
        cmds.checkBox('manual_adjustment', edit=True, enable=False)
        
    def Number_enable_True(self, *args):
        cmds.intSliderGrp('headNumber', edit=True, enable=True)
        cmds.intSliderGrp('tailNumber', edit=True, enable=True)
        cmds.button('createJoint', edit=True, enable=True)
        cmds.checkBox('manual_adjustment', edit=True, enable=True)
        cmds.button('Run', edit=True, enable=True)
        
    #############################################################################################################
    def create_locate(self, *args):
        """
        Create three locators first, then manually position them before running to create bones
        """
        
        self.aspect = cmds.textField("aspect",  query=True, text=True)
        self.name = cmds.textField("name",  query=True, text=True)
        
        self.headNumber = cmds.intSliderGrp('headNumber', query=True, value=True)
        self.tailNumber = cmds.intSliderGrp('tailNumber', query=True, value=True)
        
        self.head_locator = 'loc_' + self.aspect +'_' + self.name + 'locateHeadLocator_001'
        self.middle_locator = 'loc_' + self.aspect +'_' + self.name + 'locateMiddleLocator_001'
        self.tail_locator = 'loc_' + self.aspect +'_' + self.name + 'locateTailLocator_001'
        
        # create world ctlrs 
        self.world_ctrl = 'ctrl_' + self.aspect +'_' + self.name +'World_001'
        
        if not cmds.objExists(self.world_ctrl):
            cmds.curve(degree=3, point=world, name=self.world_ctrl)
            world_ctrl_shape = cmds.listRelatives(self.world_ctrl, shapes=True)[0]
            self.world_ctrl_shape = cmds.rename(world_ctrl_shape, self.world_ctrl + 'Shape')

            
            # create locate locator 
            cmds.createNode('locator', name=self.head_locator + 'Shape')
            cmds.createNode('locator', name=self.middle_locator + 'Shape')
            cmds.createNode('locator', name=self.tail_locator + 'Shape')

            # set locator Initial Position
            cmds.setAttr(self.head_locator + '.translateZ', 3)
            cmds.setAttr(self.tail_locator + '.translateZ', -10)

            # head and self.tail_locator parent self.middle_locator
            cmds.parent(self.head_locator, self.middle_locator)
            cmds.parent(self.tail_locator, self.middle_locator)
            cmds.parent(self.middle_locator, self.world_ctrl)

            # add Number of segments bone attr
            cmds.addAttr(self.head_locator, longName='boneSegments', attributeType='long', 
                            min=0, defaultValue=self.headNumber, keyable=True)
            # set keyable 
            cmds.setAttr(self.head_locator + '.boneSegments', keyable=False, channelBox=True)

            cmds.addAttr(self.tail_locator, longName='boneSegments', attributeType='long', 
                            min=0, defaultValue=self.tailNumber, keyable=True)
            # set keyable 
            cmds.setAttr(self.tail_locator + '.boneSegments', keyable=False, channelBox=True)
            
            # Lock useless attributes
            for trs in ['rotate']:
                for xyz in ['X', 'Y', 'Z']:
                    cmds.setAttr(self.head_locator + '.{}{}'.format(trs, xyz), keyable=False, lock=True)
                    cmds.setAttr(self.middle_locator + '.{}{}'.format(trs, xyz), keyable=False)
                    cmds.setAttr(self.tail_locator + '.{}{}'.format(trs, xyz), keyable=False, lock=True)
            
            # Set non keyable frames
            for trs in ['translate', 'scale']:
                for xyz in ['X', 'Y', 'Z']:
                    for i in [self.head_locator, self.middle_locator, self.tail_locator]:
                        cmds.setAttr(i + '.{}{}'.format(trs, xyz), keyable=False, channelBox=True)
                        cmds.setAttr(i + '.visibility', keyable=False, channelBox=True)
                        # hide  locator shape attr 
                        locator_shape = cmds.listRelatives(i, shapes=True)[0]
                        cmds.setAttr(locator_shape + '.lp' + xyz.lower(), lock=True, keyable=False, channelBox=False)
            
            # set world ctrl default scale 
            cmds.setAttr(self.world_ctrl + '.scale', 5, 5, 5)
            self.key_enable_True()
            self.Number_enable_True()
            cmds.select(self.world_ctrl)
        else:
            cmds.warning('Objects with the same name exist in the scene')

    #############################################################################################################
    def create_master(self, *args):
        # translate name 
        self.master = 'master_' + self.aspect + '_' + self.name
        
        self.geometry = 'geometry' + self.aspect + '_' + self.name
        self.controls = 'controls' + self.aspect + '_' + self.name
        self.joints = 'joints' + self.aspect + '_' + self.name

        self.rigNodes = 'rigNodes' + self.aspect + '_' + self.name
        self.rigNodesLocal = 'rigNodesLocal' + self.aspect + '_' + self.name
        self.rigNodesWorld = 'rigNodesWorld' + self.aspect + '_' + self.name

        ########################
        cmds.createNode('transform', name=self.master)
        cmds.addAttr(self.master, ln='geometryVis', at='bool', keyable=True)
        cmds.addAttr(self.master, ln='geometryDisplayType', at='enum', en='Normal:Template:Reference', keyable=True)
        cmds.addAttr(self.master, ln='controlsVis', at='bool', keyable=True)
        cmds.addAttr(self.master, ln='jointsVis', at='bool', keyable=True)
        cmds.addAttr(self.master, ln='rigNodesVis', at='bool', keyable=True)

        # create transform add attr 
        cmds.setAttr('{0}.geometryVis'.format(self.master), 1, keyable=False, channelBox=True)
        cmds.setAttr('{0}.geometryDisplayType'.format(self.master), keyable=False, channelBox=True)
        cmds.setAttr('{0}.controlsVis'.format(self.master), 1, keyable=False, channelBox=True)
        cmds.setAttr('{0}.jointsVis'.format(self.master), 1, keyable=False, channelBox=True)
        cmds.setAttr('{0}.rigNodesVis'.format(self.master), 1, keyable=False, channelBox=True)
        cmds.setAttr(self.master + '.rigNodesVis', 0)
        ########################
        cmds.createNode('transform', name=self.geometry, parent=self.master)
        cmds.createNode('transform', name=self.controls, parent=self.master)
        ########################
        cmds.createNode('transform', name=self.joints, parent=self.master)
        ########################
        cmds.createNode('transform', name=self.rigNodes, parent=self.master)
        cmds.createNode('transform', name=self.rigNodesLocal, parent=self.rigNodes)
        cmds.createNode('transform', name=self.rigNodesWorld, parent=self.rigNodes)
        ########################
        # master connect transform
        for connect_v in zip(['geometryVis', 'controlsVis', 'rigNodesVis'], [self.geometry, self.controls, self.rigNodes]):
            cmds.connectAttr('{0}.{1}'.format(self.master, connect_v[0]), '{0}.visibility'.format(connect_v[1]))

        # connect geometrt show type attr
        cmds.setAttr('{0}.overrideEnabled'.format(self.geometry), 1)
        cmds.connectAttr('{0}.geometryDisplayType'.format(self.master), '{0}.overrideDisplayType'.format(self.geometry))

        cmds.parentConstraint(self.world_ctrl, self.rigNodesLocal, weight=1)
    
    def create_joints(self, *args):
        ########################################2-create body Curve To body bone###############################################
        # create curve 
        self.body_curve = self.createCurve([self.middle_locator, self.tail_locator], name='curve_' + self.aspect + '_' + self.name + '_001')
        
        # hide body_curve
        cmds.setAttr(self.body_curve + '.visibility', 0)
        # create bone 
        get_tail_boneSegments = cmds.getAttr(self.tail_locator + '.boneSegments')
        # rebuildCurve 
        cmds.rebuildCurve(self.body_curve, constructionHistory=True, replaceOriginal=True, rebuildType=0, endKnots=1, 
                            keepRange=0, keepControlPoints=False, keepEndPoints=True, keepTangents=False, spans=get_tail_boneSegments - 3, 
                                degree=3, tolerance=0.01)
        
        # get body curve cv point 
        self.body_curve_cv = cmds.ls(self.body_curve + '.cv[*]', flatten=True)

        self.body_jnt_lit = []
        for i, cv_i in enumerate(self.body_curve_cv):
            # get body curve cv translate 
            cv_translate = cmds.xform(cv_i, query=True, translation=True, worldSpace=True)
            # create bone 
            body_jnt = cmds.createNode('joint', name='jnt_' + self.aspect + '_' + self.name + 'Body_{:03d}'.format(i + 1))
            # set body curve cv translate 
            cmds.xform(body_jnt, translation=cv_translate, worldSpace=True)
            self.body_jnt_lit.append(body_jnt)

        # Create hierarchical relationships
        for i in range(len(self.body_jnt_lit)):
            try:
                cmds.parent(self.body_jnt_lit[i + 1], self.body_jnt_lit[i])
            except:
                pass 

        # orient joint
        cmds.joint(self.body_jnt_lit[0], edit=True, orientJoint='xyz', secondaryAxisOrient='yup', children=True, zeroScaleOrient=True)
        cmds.setAttr(self.body_jnt_lit[-1] + '.jointOrient', 0, 0, 0)

        ########################################2-1create head Curve To body bone###############################################
        # create bone 
        get_head_boneSegments = cmds.getAttr(self.head_locator + '.boneSegments') + 2
        get_v = self.bisection_value(get_head_boneSegments)
        snakebody_neck_bone_lit = []
        for head, i in enumerate(get_v):
            # create bone
            snakebody_bone = cmds.createNode('joint', name='jnt_' + self.aspect + '_' + self.name + 'Neck_{:03d}'.format(head + 1))
            # parentConstraint
            pc = cmds.parentConstraint(self.middle_locator, self.head_locator, snakebody_bone, weight=1)[0]
            # set w0 w1
            cmds.setAttr(pc + '.w0', 1 - i)
            cmds.setAttr(pc + '.w1', i)
            
            cmds.delete(pc)
            snakebody_neck_bone_lit.append(snakebody_bone)
            cmds.makeIdentity(snakebody_bone, apply=True, rotate=True)
            
            # master jointsVis connect neck head skin bone 
            cmds.connectAttr(self.master + '.jointsVis', snakebody_bone + '.visibility')
            
        # Create hierarchical relationships
        for i in range(len(snakebody_neck_bone_lit)):
            try:
                cmds.parent(snakebody_neck_bone_lit[i + 1], snakebody_neck_bone_lit[i])
            except:
                pass

        # orient joint
        cmds.joint(snakebody_neck_bone_lit[0], edit=True, orientJoint='xyz', secondaryAxisOrient='yup', children=True, zeroScaleOrient=True)
        cmds.setAttr(snakebody_neck_bone_lit[-1] + '.jointOrient', 0, 0, 0)
        
        # create body root locator
        self.snakebody_loc_name = 'loc_' + self.aspect + '_' + self.name + 'Body_001'
        self.snakebody_zero = cmds.createNode('transform', name=self.snakebody_loc_name.replace('loc_', 'zero_'))
        self.hideJnt_zero = cmds.createNode('transform', name='zero_' + self.aspect + '_' + self.name + '_HideJnt_001')
        self.snakebody_loc = cmds.createNode('locator', name=self.snakebody_loc_name + 'Shape')
        
        # hide loc shapes 
        cmds.setAttr(self.snakebody_loc + '.visibility', 0)
        cmds.parent(self.snakebody_loc_name, self.snakebody_zero)
        cmds.parent(self.hideJnt_zero, self.snakebody_loc_name)
        # hide hideJnt_zero
        cmds.setAttr(self.hideJnt_zero + '.visibility', 0)
        # set snakebody_loc translate
        cmds.delete(cmds.parentConstraint(self.middle_locator, self.snakebody_zero, weight=1))
        # set hideJnt_zero translate
        cmds.delete(cmds.parentConstraint(self.snakebody_loc_name, self.hideJnt_zero, weight=1))
        # create bone parent snakebody loc 
        cmds.parent(self.body_jnt_lit[0], self.snakebody_loc_name)
        cmds.parent(snakebody_neck_bone_lit[0], self.snakebody_loc_name)
        # set snakebody_loc translate
        cmds.delete(cmds.parentConstraint(self.middle_locator, self.snakebody_zero, weight=1))

        # get head joint
        snakebody_head_bone_lit = []
        for i, ii in enumerate(snakebody_neck_bone_lit[-2:]):
            split_name = ii.split('_')
            new_name = split_name[0] + '_'+ self.aspect + '_' + self.name + 'Head_{:03d}'.format(i + 1)
            snakebody_head_bone_lit.append(new_name)
            # rename 
            cmds.rename(ii, new_name)

        # replace neck -1 -2 name  
        self.new_snakebody_neck_bone_lit = []
        for i, ii in enumerate(snakebody_neck_bone_lit):
            if i != len(snakebody_neck_bone_lit) - 1 and i != len(snakebody_neck_bone_lit) - 2:
                self.new_snakebody_neck_bone_lit.append(ii)
            else:
                s = 0
                for iii in snakebody_head_bone_lit:
                    if s == 0:
                        self.new_snakebody_neck_bone_lit.append(iii)
                    s += 1

    def adjust_create_joint(self, *args):
        ######################################################################################################################
        # set self.body_curve_cv translate 
        for i in zip(self.body_jnt_lit, self.body_curve_cv):
            get_translate = cmds.xform(i[0], query=True, translation=True, worldSpace=True)
            cmds.xform(i[1], translation=get_translate, worldSpace=True)
        # show body_curve
        cmds.setAttr(self.body_curve + '.visibility', 1)

        # copy body_curve curve 
        self.spline_ik_curve = cmds.duplicate(self.body_curve, name='curve_' + self.aspect + '_' + self.name + 'SplineIk_001')
        self.spline_ik_curve_shape = cmds.listRelatives(self.spline_ik_curve, shapes=True)[0]
        
        ######################################################################################################################

    def create_neck_bone_ctrl(self, *args):
        self.fk_ctrl_lit = []
        self.fk_zero_lit = []
        
        # set self.world_ctrl Color 
        cmds.setAttr(self.world_ctrl_shape + '.overrideEnabled', 1)
        cmds.setAttr(self.world_ctrl_shape + '.overrideColor', 30)

        
        # Freeze body and neck bone axis
        for i in [self.body_jnt_lit, self.new_snakebody_neck_bone_lit]:
            for ii in i:
                cmds.makeIdentity(ii, apply=True, translate=True, rotate=True, scale=True, normal=False, preserveNormals=True)

        # get world fk scale 
        self.wordl_fk_scale = cmds.getAttr(self.world_ctrl + '.scale')
        
        for i in self.new_snakebody_neck_bone_lit[:-1]:
            jnt_name = i.replace('jnt_', 'ctrl_')
            
            # judgement ctrl shapes
            Shape = Pin2x
            Color = 14
            if i == self.new_snakebody_neck_bone_lit[-2]:
                Shape = snakehead
                Color = 17
            # create fk ctrl
            fk_ctrl = cmds.curve(d=1, p=Shape, name=jnt_name)
            # get fk_ctrl Shape 
            fk_ctrl_shape = cmds.listRelatives(fk_ctrl, shapes=True)[0]
            # rename fk ctrl shapes 
            fk_ctrl_shape = cmds.rename(fk_ctrl_shape, jnt_name + 'Shape')
            # hide visibility
            cmds.setAttr(fk_ctrl + '.visibility', lock=True, keyable=False, channelBox=False)
            # set Color 
            cmds.setAttr(fk_ctrl_shape + '.overrideEnabled', 1)
            cmds.setAttr(fk_ctrl_shape + '.overrideColor', Color)
            # set fk ctrl translate and rotate 
            cmds.matchTransform(fk_ctrl, i)
            # fk ctrl scale
            cmds.setAttr(fk_ctrl + '.scale', self.wordl_fk_scale[0][0], self.wordl_fk_scale[0][1], self.wordl_fk_scale[0][2]) 
            # fk ctrl create zero 
            fk_zero = self.Hierarchical_group(fk_ctrl)
            
            self.fk_ctrl_lit.append(fk_ctrl)
            self.fk_zero_lit.append(fk_zero)

        # fk ctrl fk zero create Hierarchical relationship
        for i in range(len(self.fk_ctrl_lit)):
            try:
                cmds.parent(self.fk_zero_lit[i + 1], self.fk_ctrl_lit[i])
            except:
                pass

        # deposit spline_ik_skin_loc grpup 
        self.spline_ik_skin_loc_grp = cmds.createNode('transform', name='grp_' + self.aspect + '_' + self.name + 'SplineIkSkinLoc_001')
        cmds.parent(self.spline_ik_skin_loc_grp, self.rigNodesWorld)
        cmds.parentConstraint(self.world_ctrl, self.spline_ik_skin_loc_grp, weight=1)
        
        # fk ctrl give self.new_snakebody_neck_bone_lit parentConstraint
        for i in zip(self.fk_ctrl_lit, self.new_snakebody_neck_bone_lit):
            pc = cmds.parentConstraint(i[0], i[1], weight=1)[0]
            cmds.connectAttr(i[0] + '.scale', i[1] + '.scale')
            cmds.setAttr(pc + '.interpType', 2)
            # lock self.fk_ctrl_lit scale X
            cmds.setAttr(i[0] + '.scaleX', lock=True, keyable=False, channelBox=False)

        # create world locator
        world_locator_name = 'loc_' + self.aspect + '_' + self.name + 'WorldLocator_001'
        cmds.createNode('locator', name=world_locator_name + 'Shape')
        # hide world_locator_name
        cmds.setAttr(world_locator_name + '.visibility', 0)

        # get head loc and tail loc the translateZ
        head_locator_translateZ = cmds.xform(self.head_locator, query=True, translation=True, worldSpace=True)[-1]
        tail_locator_translateZ = cmds.xform(self.tail_locator, query=True, translation=True, worldSpace=True)[-1]

        # Calculate scale numerical values
        world_ctrl_scale = abs(abs(head_locator_translateZ) - abs(tail_locator_translateZ)) - 1

        # world ctrl create zero 
        world_ctrl_zero = self.Hierarchical_group(self.world_ctrl)

        # neck ctrl parent world ctrl
        cmds.parent(self.fk_zero_lit[0], self.world_ctrl)
        cmds.parent(world_locator_name, self.world_ctrl)

        # world ctrl scale 
        pc = cmds.parentConstraint(world_locator_name, self.snakebody_loc_name, weight=1, maintainOffset=True)[0]
        cmds.setAttr(pc + '.interpType', 2)

        # world joints scale 
        cmds.scaleConstraint(self.world_ctrl, self.joints, weight=1, maintainOffset=True)[0]

        # Organize hierarchical relationships
        cmds.parent(world_ctrl_zero, self.controls)
        cmds.parent(self.snakebody_zero, self.joints)
        cmds.parent(self.body_curve, self.rigNodesWorld)
        cmds.parent(self.spline_ik_curve, self.rigNodesWorld)

        # world add self.rigscale attr
        self.rigscale = self.world_ctrl + '.rigscale'
        self.bodyikHandTwist = self.fk_ctrl_lit[-1] + '.bodyTwist'
        
        cmds.addAttr(self.world_ctrl, longName='rigscale', attributeType='double', defaultValue=1, keyable=True)
        cmds.addAttr(self.fk_ctrl_lit[-1], longName='bodyTwist', attributeType='double', keyable=True)
        # set world ctrl hide
        cmds.setAttr(self.world_ctrl + '.visibility', lock=True, keyable=False, channelBox=False)
        # self.rigscale connect scale XYZ
        for xyz in ['X', 'Y', 'Z']:
            cmds.connectAttr(self.rigscale, self.world_ctrl + '.scale' + xyz)
            cmds.setAttr(self.world_ctrl + '.scale' + xyz, lock=True, keyable=False, channelBox=False)
        
        ##########################################################################
        # hide and lock useless attr 
        for i in [self.master, self.geometry, self.controls, self.joints, 
                    self.rigNodes, self.rigNodesLocal, self.rigNodesWorld]:
            # hide and lock transform visibility
            cmds.setAttr(i + '.visibility', lock=True, channelBox=False, keyable=False)
            # hide and lock transform translate and rotate and scale
            for trs in ['translate', 'rotate', 'scale']:
                for xyz in ['X', 'Y', 'Z']:
                    cmds.setAttr(i + '.' + trs + xyz, lock=True, channelBox=False, keyable=False)
        
    def create_body_ik_fk(self, *args):
        ####################################################create spine ik####################################################
        # copy self.body_jnt_lit bone
        spline_ik_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        self.spline_ik_jnt_lit = []
        for i in zip(self.body_jnt_lit, spline_ik_jnt):
            split_name = i[0].split('_')
            # rename 
            spline_ik_jnt_name = cmds.rename(i[1], split_name[0] + '_' + self.aspect + '_' + self.name + 'SplineIk_' + split_name[3])
            self.spline_ik_jnt_lit.append(spline_ik_jnt_name)

        # copy self.body_jnt_lit skin bone and bone ctrl 
        self.spline_ik_skin_jnt_lit = []
        self.spline_ik_skin_ctrl_lit = []
        self.spline_ik_skin_zero_lit = []
        self.spline_ik_skin_loc_lit = []
        
        for i in self.body_jnt_lit:
            split_name = i.split('_')
            # copy spline ik skin bone
            spline_ik_skin_jnt = cmds.duplicate(i, name=split_name[0] + '_' + self.aspect + '_' + self.name + 'SplineIkSkin_' + split_name[3], 
                                                    renameChildren=True, parentOnly=True)
            # spline ik skin bone placement the world
            cmds.parent(spline_ik_skin_jnt, world=True)
            # create spline ik skin jnt ctrl 
            spline_ik_skin_ctrl = cmds.curve(d=1, p=cube, name='ctrl_' + self.aspect + '_' + self.name + 'SplineIkSkin_' + split_name[3])
            
            # create spline ik skin jnt locator Used for scaling
            spline_ik_skin_loc_name = 'loc_' + self.aspect + '_' + self.name + 'SplineIkSkin_' + split_name[3]
            spline_ik_skin_loc = cmds.createNode('locator', name=spline_ik_skin_loc_name + 'Shape')
            cmds.parent(spline_ik_skin_loc_name, self.spline_ik_skin_loc_grp)
            # set translate 
            cmds.delete(cmds.parentConstraint(i, spline_ik_skin_loc_name, weight=1))
            
            cmds.rename(cmds.listRelatives(spline_ik_skin_ctrl, shapes=True)[0], spline_ik_skin_ctrl + 'Shape')
            # set skin ctrl translate rotate
            cmds.delete(cmds.parentConstraint(spline_ik_skin_jnt, spline_ik_skin_ctrl, weight=1))
            # set ik ctrl scale
            cmds.setAttr(spline_ik_skin_ctrl + '.scale', self.wordl_fk_scale[0][0], self.wordl_fk_scale[0][1], self.wordl_fk_scale[0][2])
            # set ik ctrl zero 
            spline_ik_skin_zero = self.Hierarchical_group(spline_ik_skin_ctrl)
            # spline_ik_skin_jnt parent spline_ik_skin_ctrl
            cmds.parent(spline_ik_skin_jnt, spline_ik_skin_ctrl)
            # hide spline_ik_skin_jnt
            cmds.setAttr(spline_ik_skin_jnt[0] + '.visibility', 0)
            # lock scaleX
            cmds.setAttr(spline_ik_skin_ctrl + '.scaleX', lock=True, keyable=False, channelBox=False)
            # lock visibility
            cmds.setAttr(spline_ik_skin_ctrl + '.visibility', lock=True, keyable=False, channelBox=False)
            
            self.spline_ik_skin_jnt_lit.append(spline_ik_skin_jnt[0])
            self.spline_ik_skin_ctrl_lit.append(spline_ik_skin_ctrl)
            self.spline_ik_skin_zero_lit.append(spline_ik_skin_zero[0])
            self.spline_ik_skin_loc_lit.append(spline_ik_skin_loc_name)

        # spline_ik_skin_zero grp group
        spline_ik_skin_grp = cmds.createNode('transform', name='grp_' + self.aspect + '_' + self.name + 'SplineIkSkin_001')
        cmds.parent(self.spline_ik_skin_zero_lit, spline_ik_skin_grp)
        cmds.parent(spline_ik_skin_grp, self.world_ctrl)
        cmds.parent(self.fk_zero_lit[0], self.spline_ik_skin_ctrl_lit[0])
        # hide obj
        cmds.setAttr(cmds.listRelatives(self.fk_ctrl_lit[0], shapes=True)[0] + '.visibility', 0)
        cmds.setAttr(self.spline_ik_jnt_lit[0] + '.visibility', 0)

        # create skinCluster
        cmds.skinCluster(self.spline_ik_skin_jnt_lit, self.spline_ik_curve[0], toSelectedBones=True, maximumInfluences=1, 
                            name=self.spline_ik_curve[0].replace('curve_', 'skinCluster_'))

        ####################################################create fk####################################################
        # copy create fk bone
        copy_fk_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_bind_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_rotate_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_TailCurl_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_HeadCurl_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_Curl_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_Constraint_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_path_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        cmds.reroot(copy_path_jnt[-1])
        copy_path_jnt.reverse()
        copy_Skin_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_sinScale_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_wave_spline_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_wave_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_wave_stretch_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_wave_ik_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_stretching_ik_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)
        copy_ik_spline_fusion_jnt = cmds.duplicate(self.body_jnt_lit[0], renameChildren=True)


        self.fk_jnt_lit = []
        self.hind_jnt_lit = []
        self.rotate_jnt_lit = []
        self.tailCurl_jnt_lit = []
        self.headCurl_jnt_lit = []
        self.curl_jnt_lit = []
        self.constraint_jnt_lit = []
        self.path_skin_jnt_lit = []
        self.Skin_jnt_lit = []
        self.sin_scale_jnt_lit = []
        self.waveSpline_jnt_lit = []
        self.wave_jnt_lit = []
        self.wave_stretch_jnt_lit = []
        self.wave_ik_jnt_lit = []
        self.stretching_ik_jnt_lit = []
        self.ik_spline_jnt_lit = []
        for i, ii in enumerate(zip(copy_fk_jnt, copy_bind_jnt, copy_rotate_jnt, copy_TailCurl_jnt, copy_HeadCurl_jnt, copy_Curl_jnt, 
                                    copy_Constraint_jnt, copy_path_jnt, copy_Skin_jnt, copy_sinScale_jnt, copy_wave_spline_jnt, 
                                        copy_wave_jnt, copy_wave_stretch_jnt, copy_wave_ik_jnt, copy_stretching_ik_jnt, copy_ik_spline_fusion_jnt)):
            split_name = ii[0].split('_')
            # fk bone rename
            fk_jnt = cmds.rename(ii[0], 'ctrl_' + self.aspect + '_' + split_name[2] + 'Fk_{:03d}'.format(i + 1))
            self.fk_jnt_lit.append(fk_jnt)
            # create fk ctrl shapes
            fk_ctrl = cmds.curve(degree=1, point=circle)
            # set fk ctrl scale
            cmds.setAttr(fk_ctrl + '.scale', self.wordl_fk_scale[0][0], self.wordl_fk_scale[0][1], self.wordl_fk_scale[0][2])
            # makeIdentity
            cmds.makeIdentity(fk_ctrl, apply=True, scale=True)
            # get fk ctrl shapes
            fk_ctrl_shape = cmds.listRelatives(fk_ctrl, shapes=True)[0]
            # rename fk ctrl shapes
            fk_ctrl_shape = cmds.rename(fk_ctrl_shape, 'ctrl_' + self.aspect + '_' + split_name[2] + 'Fk_{:03d}'.format(i + 1) + 'Shape')
            # fk ctrl shapes parent 
            cmds.parent(fk_ctrl_shape, fk_jnt, relative=True, shape=True)
            # delete fk ctrl transform
            cmds.delete(fk_ctrl)
            # set fk jnt drawStyle
            cmds.setAttr(fk_jnt + '.drawStyle', 2)
            # lock scaleX
            for scale_XYZ in ['X', 'Y', 'Z']:
                cmds.setAttr(fk_jnt + '.scale' + scale_XYZ, lock=True, keyable=False, channelBox=False)
            # lock visibility
            cmds.setAttr(fk_jnt + '.visibility', lock=True, keyable=False, channelBox=False)
            cmds.setAttr(fk_jnt + '.radi', lock=True, keyable=False, channelBox=False)
            
            # bind bone rename
            hind_jnt = cmds.rename(ii[1], 'jnt_' + self.aspect + '_' + split_name[2] + 'Hind_{:03d}'.format(i + 1))
            self.hind_jnt_lit.append(hind_jnt)
            # hind bone parnet fk bone
            cmds.parent(hind_jnt, fk_jnt)
            # hide bind bone 
            cmds.setAttr(hind_jnt + '.visibility', 0)

            
            # rotate bone rename 
            rotate_jnt = cmds.rename(ii[2], 'jnt_' + self.aspect + '_' + split_name[2] + 'Rotate_{:03d}'.format(i + 1))
            self.rotate_jnt_lit.append(rotate_jnt)
            # set fk jnt drawStyle
            cmds.setAttr(rotate_jnt + '.drawStyle', 2)
            
            
            # TailCurl bone rename 
            tailCurl_jnt = cmds.rename(ii[3], 'jnt_' + self.aspect + '_' + split_name[2] + 'TailCurl_{:03d}'.format(i + 1))
            self.tailCurl_jnt_lit.append(tailCurl_jnt)
            # set fk jnt drawStyle
            cmds.setAttr(tailCurl_jnt + '.drawStyle', 2)
            
            
            # TailCurl bone rename 
            headCurl_jnt = cmds.rename(ii[4], 'jnt_' + self.aspect + '_' + split_name[2] + 'HeadCurl_{:03d}'.format(i + 1))
            self.headCurl_jnt_lit.append(headCurl_jnt)
            # set fk jnt drawStyle
            cmds.setAttr(headCurl_jnt + '.drawStyle', 2)
            
            
            # Curl bone rename 
            curl_jnt = cmds.rename(ii[5], 'jnt_' + self.aspect + '_' + split_name[2] + 'Curl_{:03d}'.format(i + 1))
            self.curl_jnt_lit.append(curl_jnt)
            # set fk jnt drawStyle
            cmds.setAttr(curl_jnt + '.drawStyle', 2)
            
            
            # Fk Constraint bone rename 
            constraint_jnt = cmds.rename(ii[6], 'jnt_' + self.aspect + '_' + split_name[2] + 'FkConstraint_{:03d}'.format(i + 1))
            self.constraint_jnt_lit.append(constraint_jnt)
            # set fk jnt drawStyle
            cmds.setAttr(constraint_jnt + '.drawStyle', 2)
            
            # path bone rename 
            path_jnt = cmds.rename(ii[7], 'jnt_' + self.aspect + '_' + split_name[2] + 'Path_{:03d}'.format(i + 1))
            self.path_skin_jnt_lit.append(path_jnt)
            
            # Skin bone rename 
            Skin_jnt = cmds.rename(ii[8], 'jnt_' + self.aspect + '_' + split_name[2] + 'Skin_{:03d}'.format(i + 1))
            self.Skin_jnt_lit.append(Skin_jnt)
            # master jointsVis connect body skin bone 
            cmds.connectAttr(self.master + '.jointsVis', Skin_jnt + '.visibility')
            
            # Skin bone parnet fk bone
            cmds.parent(Skin_jnt, fk_jnt)

            # sin scale bone rename 
            sin_scale_jnt = cmds.rename(ii[9], 'jnt_' + self.aspect + '_' + split_name[2] + 'SinScale_{:03d}'.format(i + 1))
            self.sin_scale_jnt_lit.append(sin_scale_jnt)
            # sin scale bone parnet fk bone
            cmds.parent(sin_scale_jnt, fk_jnt)
            cmds.setAttr(sin_scale_jnt + '.visibility', 0)

            
            # wave Spline bone rename 
            waveSpline_jnt = cmds.rename(ii[10], 'jnt_' + self.aspect + '_' + split_name[2] + 'WaveSpline_{:03d}'.format(i + 1))
            self.waveSpline_jnt_lit.append(waveSpline_jnt)
            
            
            # wave Spline bone rename 
            wave_jnt = cmds.rename(ii[11], 'jnt_' + self.aspect + '_' + split_name[2] + 'Wave_{:03d}'.format(i + 1))
            self.wave_jnt_lit.append(wave_jnt)
            
            # wave Spline stretch bone rename 
            wave_stretch_jnt = cmds.rename(ii[12], 'jnt_' + self.aspect + '_' + split_name[2] + 'WaveStretch_{:03d}'.format(i + 1))
            self.wave_stretch_jnt_lit.append(wave_stretch_jnt)
            
            # wave Spline Ik fusion bone rename 
            wave_ik_jnt = cmds.rename(ii[13], 'jnt_' + self.aspect + '_' + split_name[2] + 'WaveIk_{:03d}'.format(i + 1))
            self.wave_ik_jnt_lit.append(wave_ik_jnt)
            
            # stretching ik spline bone
            stretching_ik_jnt = cmds.rename(ii[14], 'jnt_' + self.aspect + '_' + split_name[2] + 'IkStretching_{:03d}'.format(i + 1))
            self.stretching_ik_jnt_lit.append(stretching_ik_jnt)
            
            # stretching ik spline fusion bone
            ik_spline_jnt = cmds.rename(ii[15], 'jnt_' + self.aspect + '_' + split_name[2] + 'IkSplineStretching_{:03d}'.format(i + 1))
            self.ik_spline_jnt_lit.append(ik_spline_jnt)
            
            
            # set shapes color
            cmds.setAttr(fk_ctrl_shape + '.overrideEnabled', 1)
            cmds.setAttr(fk_ctrl_shape + '.overrideColor', 6)



        ################################################################
        # create ik spline handle 
        self.ik_spline_handle = cmds.ikHandle(startJoint=self.ik_spline_jnt_lit[0], endEffector=self.ik_spline_jnt_lit[-1], curve=self.spline_ik_curve[0], 
                        sol='ikSplineSolver', ccv=False, scv=False, pcv=False, 
                            name='ikHand_' + self.aspect + '_' + split_name[2] + '_001')
        
        cmds.rename(self.ik_spline_handle[-1], 'effector_' + self.aspect + split_name[2] + '_001')
        cmds.parent(self.ik_spline_handle[0], self.rigNodesWorld)

        # create multDoubleLinear Multiplier value Twist
        bodyikHandTwist_mult = cmds.createNode('multDoubleLinear', name='mult_' + self.aspect + '_' + self.name + 'BodyIkHandTwist_001')
        # self.bodyikHandTwist connect body ik handle
        cmds.connectAttr(self.bodyikHandTwist, bodyikHandTwist_mult + '.input1')
        cmds.connectAttr(bodyikHandTwist_mult + '.output', self.ik_spline_handle[0] + '.twist')
        # set attr 
        cmds.setAttr(bodyikHandTwist_mult + '.input2', 10)

        # Create bones to set the stretching of Ik Spline body bones
        stretching_curve_one = cmds.duplicate(self.body_curve, name='curve_' + self.aspect + '_' + self.name + 'WavesStretchDel_001')[0]
        stretching_curve_two = cmds.duplicate(self.body_curve, name='curve_' + self.aspect + '_' + self.name + 'WavesStretchDel_002')[0]
        # curve parent to world controller
        cmds.parent([stretching_curve_one, stretching_curve_two], self.world_ctrl)

        # set stretching curve translate and rotate 
        # ger tranlate 
        rotate_pivot = cmds.xform(self.world_ctrl, query=True, translation=True, worldSpace=True)
        for i in [stretching_curve_one, stretching_curve_two]:
            # freeze attr
            cmds.makeIdentity(i, apply=True, t=True, r=True)
            # get curve translate 
            cmds.setAttr(i + '.rotatePivot', rotate_pivot[0], rotate_pivot[1], rotate_pivot[2])
            #cmds.setAttr(i + '.translate', 0, 0, 0)
            #cmds.setAttr(i + '.rotate', 0, 0, 0)
            if i == stretching_curve_one:
                cmds.setAttr(i + '.translate', 0, 1, 0)
            else:
                cmds.setAttr(i + '.translate', 0, -1, 0)
            cmds.parent(i, world=True)

        # create nurbsSurface
        stretching_surface = 'surface_' + self.aspect + '_' + self.name + 'IkSplineStretching_001'
        self.nurbsSurface(stretching_curve_one, stretching_curve_two, stretching_surface)
        # get stretching_surface shape
        stretching_surface_shape = cmds.listRelatives(stretching_surface, shapes=True)[0]
        # delete stretching curve
        cmds.delete(stretching_curve_one, stretching_curve_two)
        # create stretching surface parent to rigNodesWorld
        cmds.parent(stretching_surface, self.rigNodesWorld)
        # create group placement stretching foll
        stretching_group = cmds.createNode('transform', name='grp_' + self.aspect + '_' + self.name + 'StretchingFoll_001')
        ik_spline_constraint_lit = []
        for i in enumerate(self.stretching_ik_jnt_lit):
            UV = self.get_UV(stretching_surface, i[1])
            foll_name = self.create_foll_setUV(i[0] + 1, stretching_surface, UV[0], UV[1], 'Stretching')
            cmds.parent(foll_name, stretching_group)
            # stretching foll parentConstraint self.stretching_ik_jnt_lit
            ik_spline_constraint = cmds.parentConstraint(foll_name, i[1], maintainOffset=True, weight=1)[0] 
            cmds.setAttr(ik_spline_constraint + '.interpType', 2)
            
            ik_spline_constraint_lit.append(ik_spline_constraint)
            
        # stretching_group placement rigNodesWorld
        cmds.parent(stretching_group, self.rigNodesWorld)

        #  stretching_surface create skinClust  
        cmds.skinCluster(self.spline_ik_skin_jnt_lit, stretching_surface, toSelectedBones=True, maximumInfluences=1, 
                            name='skinClust_' + self.aspect + '_' + self.name + 'IkSplineStretching_001')

        # Stretching bone no Stretching Fusion onto the final bone
        stretching_ik_spline_Point_lit = []
        for i in zip(self.stretching_ik_jnt_lit, self.ik_spline_jnt_lit, self.spline_ik_jnt_lit):
            stretching_ik_spline_Point = cmds.pointConstraint(i[0], i[1], i[2], weight=1)[0]
            stretching_ik_spline_Orient = cmds.orientConstraint(i[1], i[2], offset=[0, 0, 0], weight=1)[0]
            cmds.setAttr(stretching_ik_spline_Orient + '.interpType', 2)
            
            stretching_ik_spline_Point_lit.append(stretching_ik_spline_Point)

        # Hide the hidden bone
        cmds.parent([self.stretching_ik_jnt_lit[0], self.ik_spline_jnt_lit[0]], self.hideJnt_zero)

        ####################### spline ik bone create stretch  ########################
        # world ctrl add stretch attr
        cmds.addAttr(self.world_ctrl, longName='ikStretch', attributeType='enum', enumName=' ' , niceName='Ik Stretch----------', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='stretch', attributeType='float', min=0, max=1, defaultValue=1, keyable=True)

        world_ctrl_stretch = self.world_ctrl + '.stretch'

        # Set ik spline bone properties for stretching on - off
        ik_spline_stretching_reverse = cmds.createNode('reverse', name='reve_' + self.aspect + '_' + self.name + 'IkSplineStretching_001')
        cmds.connectAttr(world_ctrl_stretch, ik_spline_stretching_reverse + '.inputX')
        for i in stretching_ik_spline_Point_lit:
            cmds.connectAttr(world_ctrl_stretch, i + '.w0')
            cmds.connectAttr(ik_spline_stretching_reverse + '.outputX', i + '.w1')

        ################################################################

        # hide spine ik bone 
        cmds.setAttr(self.spline_ik_jnt_lit[0] + '.visibility', 0)

        # hide bone
        cmds.setAttr(self.constraint_jnt_lit[0] + '.visibility', 0)
        cmds.setAttr(self.path_skin_jnt_lit[0] + '.visibility', 0)
        cmds.setAttr(self.wave_stretch_jnt_lit[0] + '.visibility', 0)
        cmds.setAttr(self.wave_ik_jnt_lit[0] + '.visibility', 0)

        # Hind bone create set 
        self.Skin_Bone_Set = cmds.sets(self.new_snakebody_neck_bone_lit, self.Skin_jnt_lit[1:], 
                                    name='set_' + self.aspect + '_' + self.name + '_Skin_Bone')
        
        # hide self.Skin_jnt_lit[0] 
        cmds.setAttr(self.Skin_jnt_lit[0] + '.drawStyle', 2)

    def create_creep_function(self, *args):
        # Controlled attribute direction
        sin_translate = 'translateZ'
        curl_rotate = 'rotateY'

        # self.world_ctrl add attr
        world_ctrl_width = self.world_ctrl + '.width'
        world_ctrl_speed = self.world_ctrl + '.speed'
        world_ctrl_go = self.world_ctrl + '.go'
        world_ctrl_delay = self.world_ctrl + '.delay'
        world_ctrl_addWidth = self.world_ctrl + '.addWidth'

        world_ctrl_rotX = self.world_ctrl + '.rotX'
        world_ctrl_rotY = self.world_ctrl + '.rotY'
        world_ctrl_rotZ = self.world_ctrl + '.rotZ'

        world_ctrl_tailBend = self.world_ctrl + '.tailBend'
        world_ctrl_tailBendAngle = self.world_ctrl + '.tailBendAngle'
        world_ctrl_tailFalloff = self.world_ctrl + '.tailFalloff'

        world_ctrl_headBend = self.world_ctrl + '.headBend'
        world_ctrl_headBendAngle = self.world_ctrl + '.headBendAngle'
        world_ctrl_headFalloff = self.world_ctrl + '.headFalloff'

        world_ikCtrlVis = self.world_ctrl + '.ikCtrlVis'
        world_partIkCtrlVis = self.world_ctrl + '.partIkCtrlVis'
        world_fkCtrlVis = self.world_ctrl + '.fkCtrlVis'

        self.world_path = self.world_ctrl + '.pathCtrlVis'
        self.world_offset = self.world_ctrl + '.offset'
        
        # addr attr
        cmds.addAttr(self.world_ctrl, longName='sinAttr', niceName='Sin Attr----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='width', attributeType='float', min=-10, max=10, defaultValue=0, keyable=True)
        cmds.addAttr(self.world_ctrl, longName='speed', attributeType='float',min=-10, max=10, keyable=True)
        cmds.addAttr(self.world_ctrl, longName='go', attributeType='float', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='delay', attributeType='float', min=0, defaultValue=0.5, keyable=True)
        cmds.addAttr(self.world_ctrl, longName='addWidth', attributeType='float', defaultValue=-0.025, keyable=True)

        cmds.addAttr(self.world_ctrl, longName='rotateAttr', niceName='Rotate Attr----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='rotX', attributeType='float', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='rotY', attributeType='float', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='rotZ', attributeType='float', keyable=True)

        cmds.addAttr(self.world_ctrl, longName='ctrlsVisShowHide', niceName='Ctrls Vis Show Hide----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='ikCtrlVis', attributeType='bool', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='partIkCtrlVis', attributeType='bool', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='fkCtrlVis', attributeType='bool', keyable=True)

        # create a curve as a path animation
        cmds.addAttr(self.world_ctrl, longName='pathAttr', niceName='Path Attr----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='pathCtrlVis', attributeType='bool', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='offset', attributeType='float', min=0, max=100, defaultValue=0, keyable=True)


        # set attr
        cmds.setAttr(self.world_ctrl + '.sinAttr', lock=True)
        cmds.setAttr(self.world_ctrl + '.rotateAttr', lock=True)
        cmds.setAttr(self.world_ctrl + '.ctrlsVisShowHide', lock=True)
        cmds.setAttr(self.world_ctrl + '.pathAttr', lock=True)
        cmds.setAttr(world_ctrl_delay, keyable=False, channelBox=True)
        cmds.setAttr(world_ctrl_addWidth, keyable=False, channelBox=True)
        cmds.setAttr(world_ikCtrlVis, keyable=False, channelBox=True)
        cmds.setAttr(world_partIkCtrlVis, keyable=False, channelBox=True)
        cmds.setAttr(world_fkCtrlVis, keyable=False, channelBox=True)
        cmds.setAttr(self.world_path, keyable=False, channelBox=True)
        cmds.setAttr(world_ikCtrlVis, 1)
        cmds.setAttr(world_partIkCtrlVis, 1)
        cmds.setAttr(world_fkCtrlVis, 1)
        cmds.setAttr(self.world_path, 1)

        #######################################################################
        # Find if there is an object with the same name in the scene
        split_name = self.world_ctrl.split('_')
        exp_sin = 'exp_' + self.aspect + '_' + self.name + 'Sin_' + split_name[3]
        if not cmds.objExists(exp_sin):
            cmds.createNode('expression', name=exp_sin)
            
        # sin Organizational Expression Code
        expression_sin = ''
        for i, ii in enumerate(self.spline_ik_skin_zero_lit):
            connect = ii.replace('zero_', 'connect_')
            ctrl = ii.replace('zero_', 'ctrl_')
            # add Local Control Properties
            ik_Local = ctrl + '.widthRG'
            cmds.addAttr(ctrl, longName='widthRG', attributeType='float', defaultValue=1, keyable=True)
            
            
            string = '{}.{}=sin(time*{}+{}-{}*{})*{}*(1+{}*{})*{};\n'.format(connect, sin_translate, world_ctrl_speed, world_ctrl_go, i, world_ctrl_delay, world_ctrl_width, 
                                                                    i, world_ctrl_addWidth, ik_Local)
            expression_sin += string
            
        # add expression string
        cmds.expression(exp_sin, edit=True, string=expression_sin, alwaysEvaluate=1, unitConversion='all')

        # wordl_ctrl rox roy roz attr connect rotate_jnt rotateX rotateY rotateZ
        for i in self.rotate_jnt_lit:
            cmds.connectAttr(world_ctrl_rotX, i + '.rotateX')
            cmds.connectAttr(world_ctrl_rotY, i + '.rotateY')
            cmds.connectAttr(world_ctrl_rotZ, i + '.rotateZ')


        # set Hierarchical relationship 
        for i in range(len(self.fk_jnt_lit)):
            try:
                cmds.parent(self.rotate_jnt_lit[i], self.fk_jnt_lit[i])
                cmds.parent(self.fk_jnt_lit[i + 1], self.rotate_jnt_lit[i])
            except:
                pass

        #######################################################################

        # tail curl Organizational Expression Code
        # sort descending
        cmds.addAttr(self.world_ctrl, longName='tailBendAttr', niceName='Tail Bend Attr----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.setAttr(self.world_ctrl + '.tailBendAttr', lock=True)
        tail_distr = self.trntacleRoll(self.world_ctrl, self.tailCurl_jnt_lit, 'Tail')


        # head curl Organizational Expression Code
        # sort descending
        self.headCurl_jnt_lit.reverse()
        cmds.addAttr(self.world_ctrl, longName='headBendAttr', niceName='Head Bend Attr----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.setAttr(self.world_ctrl + '.headBendAttr', lock=True)
        head_distr = self.trntacleRoll(self.world_ctrl, self.headCurl_jnt_lit, 'Head')

        # Create a sets for easy setup
        self.Distr_Node_Set = cmds.sets(tail_distr, head_distr, name='Set_' + self.aspect + '_' + self.name + '_Distr_Node')
        
        #######################################################################Here Stuck 
        # tail curl bone Create Hierarchy
        for i in range(len(self.tailCurl_jnt_lit)):
            try:
                cmds.parent(self.fk_jnt_lit[i], self.tailCurl_jnt_lit[i])
                cmds.parent(self.tailCurl_jnt_lit[i+1], self.rotate_jnt_lit[i])
            except:
                pass

        self.headCurl_jnt_lit.reverse()
        # head curl bone Create Hierarchy
        for i in range(len(self.headCurl_jnt_lit)):
            try:
                cmds.parent(self.tailCurl_jnt_lit[i], self.headCurl_jnt_lit[i])
                cmds.parent(self.headCurl_jnt_lit[i+1], self.rotate_jnt_lit[i])
            except:
                pass

        # curl bone Create Hierarchy
        for i in range(len(self.curl_jnt_lit)):
            try:
                cmds.parent(self.headCurl_jnt_lit[i], self.curl_jnt_lit[i])
                cmds.parent(self.curl_jnt_lit[i+1], self.rotate_jnt_lit[i])
            except:
                pass
        #######################################################################


        # curl Constraint Fk constraint bone
        for i in zip(self.spline_ik_jnt_lit, self.constraint_jnt_lit):
            pc = cmds.parentConstraint(i[0], i[1], weight=1)[0]
            cmds.setAttr(pc + '.interpType', 2)

        # curl bone connect Fk constraint bone
        for i in zip(self.constraint_jnt_lit, self.curl_jnt_lit):
            cmds.connectAttr(i[0] + '.translate', i[1] + '.translate')
            cmds.connectAttr(i[0] + '.rotate', i[1] + '.rotate')

        # connect ctrls show hide attr
        # create condition Identify hidden switches
        cond_hide = cmds.createNode('condition', name='condi_' + self.aspect + '_' + self.name + 'JudgementHideBodeFk_001')
        # connect 
        cmds.connectAttr(world_fkCtrlVis, cond_hide + '.secondTerm')
        cmds.connectAttr(self.master + '.' + 'controlsVis', cond_hide + '.colorIfFalseR')
        for i in self.fk_jnt_lit:
            # get fk jnt shape
            shapes = cmds.listRelatives(i, shapes=True)[0]
            # connect 
            cmds.connectAttr(cond_hide + '.outColorR', shapes + '.visibility')


        subtraction = []
        for i in range(0, len(self.spline_ik_skin_ctrl_lit), 4):
            subtraction.append(self.spline_ik_skin_ctrl_lit[i])

        new_spline_ik_skin_ctrl_lit = list(set(self.spline_ik_skin_ctrl_lit) - set(subtraction))
        new_spline_ik_skin_ctrl_lit.sort()

        # create condition Show Hide IK bone Ctrl Shape
        show_hide_IkSpline = cmds.createNode('condition', name='condi_' + self.aspect + '_' + self.name + 'ShowHideIkSpline_001')
        # connect 
        cmds.connectAttr(world_ikCtrlVis, show_hide_IkSpline + '.colorIfFalseR')
        cmds.connectAttr(world_partIkCtrlVis, show_hide_IkSpline + '.firstTerm')

        for i in new_spline_ik_skin_ctrl_lit:
            # get ik jnt ctrl shape
            shape = cmds.listRelatives(i, shapes=True)[0]
            # connect 
            cmds.connectAttr(show_hide_IkSpline + '.outColorR', shape + '.visibility')

        # create node parent constraint locator
        self.interval_lit = []
        self.remove_interval_lit = []

        for i in subtraction:
            split_name = i.split('_')
            # create transform
            parent_zero = cmds.createNode('transform', name='zero_' + self.aspect + '_' + self.name + 'ParentConstraint_' + split_name[3])
            locator_name = 'loc_' + self.aspect + '_' + self.name + 'ParentConstraint_' + split_name[3]
            # create locator
            parent_locator = cmds.createNode('locator', name=locator_name + 'Shape')
            # parent
            cmds.parent(locator_name, parent_zero)
            # parent
            cmds.parent(parent_zero, i.replace('ctrl_', 'zero_'))
            # set translate rotate 0 0 0
            cmds.setAttr(parent_zero + '.translate', 0, 0, 0)
            cmds.setAttr(parent_zero + '.rotate', 0, 0, 0)
            # connect zero 
            cmds.connectAttr(i + '.translate', parent_zero + '.translate')
            cmds.connectAttr(i + '.rotate', parent_zero + '.rotate')
            # hide parentconstraint locator zero group
            cmds.setAttr(parent_zero + '.visibility', 0)
            
            # get ik jnt ctrl shape
            shapes = cmds.listRelatives(i, shapes=True)[0]
            # connect 
            cmds.connectAttr(world_ikCtrlVis, shapes + '.visibility')

            # get tail
            digit_split = i.split('_')[-1]
            self.interval_lit.append(int(digit_split))
            
            # set shapes color
            shapes = cmds.listRelatives(i, shapes=True)[0]
            cmds.setAttr(shapes + '.overrideEnabled', 1)
            cmds.setAttr(shapes + '.overrideColor', 13)


        self.mian_ik_ctrl_lit = []
        for i in new_spline_ik_skin_ctrl_lit:
            digit_split = i.split('_')[-1]
            self.remove_interval_lit.append(int(digit_split))


        jnt_Hind_scale_lit = []
        WW = [0.75, 0.5, 0.25]
        for i in self.interval_lit:
            seek = self.interval_lit.index(i)
            if i != self.interval_lit[-1]:
                big = i + 1
                small = self.interval_lit[seek + 1]
            else:
                big = i + 1
                small = self.remove_interval_lit[-1] + 1

            pc_A = []
            for ii in range(big, small):
                pc_A.append(ii)
                
            for iii in zip(pc_A, WW):
                # set parentConstraint
                split = subtraction[0].split('_')
                loc_head = locator_name.split('_')
                drv_name = 'driven_' + split[1] + '_' + split[2] + '_{:03d}'.format(iii[0])
                pc_head_name = loc_head[0] + '_' + loc_head[1] + '_' + loc_head[2] + '_{:03d}'.format(i)
                if i != self.interval_lit[-1]:
                    pc_tial_name = loc_head[0] + '_' + loc_head[1] + '_' + loc_head[2] + '_{:03d}'.format(self.interval_lit[seek+1])
                # parentConstraint 
                if i != self.interval_lit[-1]:
                    pc = cmds.parentConstraint(pc_head_name, pc_tial_name, drv_name, weight=1, maintainOffset=True)[0]
                    # set W0 - W1
                    cmds.setAttr(pc + '.w0', iii[1])
                    cmds.setAttr(pc + '.w1', abs(iii[1] - 1))
                else:
                    pc = cmds.parentConstraint(pc_head_name, drv_name, weight=1, maintainOffset=True)[0]
                
                if not self.mian_ik_ctrl_lit.count(pc_head_name):
                    self.mian_ik_ctrl_lit.append(pc_head_name)
                
                # lock ik part ctrl rotate 
                for lock_i in ['X', 'Y', 'Z']:
                    cmds.setAttr(drv_name.replace('driven_', 'ctrl_') + '.rotate' + lock_i, lock=True, keyable=False, channelBox=False)
                
                # amplify  ik ctrl Primary controller
                scale_name = drv_name.replace('driven_', 'ctrl_')
                scale_translate = cmds.xform(scale_name, query=True, translation=True, worldSpace=True)
                # get scale point cv
                point_cv = cmds.ls(scale_name + '.cv[*]', flatten=True)
                cmds.select(point_cv)
                cmds.scale(1, -0.75, -0.75, relative=True, pivot=[scale_translate[0], scale_translate[1], scale_translate[2]])
                # set parentConstraint interpType
                cmds.setAttr(pc + '.interpType', 2)
                # set shapes color
                shapes = cmds.listRelatives(scale_name, shapes=True)[0]
                cmds.setAttr(shapes + '.overrideEnabled', 1)
                cmds.setAttr(shapes + '.overrideColor', 20)
                
                
                # set scaleConstraint
                jnt = self.hind_jnt_lit[0].split('_')
                ctrl_head = self.spline_ik_skin_loc_lit[0].split('_')
                jnt_name = jnt[0] + '_' + jnt[1] + '_' + jnt[2] + '_{:03d}'.format(iii[0])
                ctrl_name = 'loc_' + ctrl_head[1] + '_' + ctrl_head[2] + '_{:03d}'.format(iii[0])
                pc_head_name = ctrl_head[0] + '_' + ctrl_head[1] + '_' + ctrl_head[2] + '_{:03d}'.format(i)
                
                if i != self.interval_lit[-1]:
                    pc_tial_name = ctrl_head[0] + '_' + ctrl_head[1] + '_' + ctrl_head[2] + '_{:03d}'.format(self.interval_lit[seek+1])
                # parentConstraint 
                if i != self.interval_lit[-1]:
                    pc_jnt = cmds.scaleConstraint(pc_head_name, pc_tial_name, jnt_name, maintainOffset=True, skip='x', weight=1)[0]
                    pc_loc = cmds.scaleConstraint(pc_head_name, pc_tial_name, ctrl_name, maintainOffset=True, skip='x', weight=1)[0]
                    
                    # set jnt W0 - W1
                    cmds.setAttr(pc_jnt + '.w0', iii[1])
                    cmds.setAttr(pc_jnt + '.w1', abs(iii[1] - 1))
                    # set ctrl W0 - W1
                    cmds.setAttr(pc_loc + '.w0', iii[1])
                    cmds.setAttr(pc_loc + '.w1', abs(iii[1] - 1))
                    
                    jnt_Hind_scale_lit.append(pc_jnt)
                    
                else:
                    pc_jnt = cmds.scaleConstraint(pc_head_name, pc_tial_name, jnt_name, maintainOffset=True, skip='x', weight=1)[0]
                    pc_loc = cmds.scaleConstraint(pc_head_name, pc_tial_name, ctrl_name, maintainOffset=True, skip='x', weight=1)[0]
                    
                    jnt_Hind_scale_lit.append(pc_jnt)
                
                # set connect rotare
                jnt = self.hind_jnt_lit[0].split('_')
                ctrl_head = self.spline_ik_skin_loc_lit[0].split('_')
                jnt_name = jnt[0] + '_' + jnt[1] + '_' + jnt[2] + '_{:03d}'.format(iii[0])
                pc_head_name = ctrl_head[0] + '_' + ctrl_head[1] + '_' + ctrl_head[2] + '_{:03d}'.format(i)
                if i != self.interval_lit[-1]:
                    pc_tial_name = ctrl_head[0] + '_' + ctrl_head[1] + '_' + ctrl_head[2] + '_{:03d}'.format(self.interval_lit[seek+1])
                
                
                # parentConstraint 
                if i != self.interval_lit[-1]:
                    # create node
                    mult_upper = cmds.createNode('multDoubleLinear', name='mult_' + ctrl_head[1] + '_' + ctrl_head[2] + 'Upper_{:03d}'.format(i))
                    mult_lower = cmds.createNode('multDoubleLinear', name='mult_' + ctrl_head[1] + '_' + ctrl_head[2] + 'Lower_{:03d}'.format(i))
                    add_lower = cmds.createNode('addDoubleLinear', name='add_' + ctrl_head[1] + '_' + ctrl_head[2] + 'middle_{:03d}'.format(i))
                    # connect node
                    cmds.connectAttr(pc_head_name + '.rotateX', mult_upper + '.input1')
                    cmds.connectAttr(pc_tial_name + '.rotateX', mult_lower + '.input1')
                    cmds.connectAttr(mult_upper + '.output', add_lower + '.input1')
                    cmds.connectAttr(mult_lower + '.output', add_lower + '.input2')
                    cmds.connectAttr(add_lower + '.output', jnt_name + '.rotateX')
                    # set input2
                    cmds.setAttr(mult_upper + '.input2', iii[1])
                    cmds.setAttr(mult_lower + '.input2', abs(iii[1] - 1))
                else:
                    cmds.connectAttr(pc_tial_name + '.rotateX', jnt_name + '.rotateX')
            
            
            # ik ctrl scaleConstraint Hind Bone
            cmds.scaleConstraint(self.spline_ik_skin_loc_lit[i-1], self.hind_jnt_lit[i-1], maintainOffset=True, skip='x', weight=1)
            # ik ctrl connect Hind Bone rotateX
            cmds.connectAttr(self.spline_ik_skin_ctrl_lit[i-1] + '.rotateX', self.hind_jnt_lit[i-1] + '.rotateX')

        self.mian_ik_ctrl_lit.append(self.spline_ik_skin_ctrl_lit[-1])
        cmds.select(clear=True)

    def create_path_curve_animation(self, *args):
        # get ik ctrl translate 
        ik_ctrl_translate_lit = []
        # reversal list
        for i in self.mian_ik_ctrl_lit:
            # get translate 
            translate = cmds.xform(i, query=True, translation=True, worldSpace=True)
            ik_ctrl_translate_lit.append(translate)

        path_jnt_lit = []
        ik_ctrl_translate_lit.reverse()
        # create locator and set locator translate 
        for i, ii in enumerate(ik_ctrl_translate_lit):
            locator_name = 'jnt_' + self.aspect + '_' + self.name + 'PathAnimation_{:03d}'.format(i+1)
            # create locator
            path_locator = cmds.createNode('joint', name=locator_name)
            cmds.parent(locator_name, self.world_ctrl)
            # set rotate transla zero
            cmds.setAttr(locator_name + '.rotate', 0, 0, 0)
            cmds.setAttr(locator_name + '.translate', 0, 0, 0)
            # set locator translate 
            cmds.xform(locator_name, translation=ii, worldSpace=True)
            path_jnt_lit.append(locator_name)

        # calculate spacing
        spacing = cmds.getAttr(path_jnt_lit[-1] + '.translateZ') - cmds.getAttr(path_jnt_lit[-2] + '.translateZ')
        A = 1
        for i in range(len(ik_ctrl_translate_lit) + 1, 30):
            locator_name = 'jnt_' + self.aspect + '_' + self.name + 'PathAnimation_{:03d}'.format(i)
            # create locator
            path_locator = cmds.createNode('joint', name=locator_name)
            cmds.parent(locator_name, self.world_ctrl)
            # set rotate transla zero
            translateZ = spacing * A
            cmds.setAttr(locator_name + '.rotate', 0, 0, 0)
            cmds.setAttr(locator_name + '.translate', 0, 0, abs(translateZ))
            
            path_jnt_lit.append(locator_name)
            A += 1

        self.path_curve = self.createCurve(path_jnt_lit, 'curve_' + self.aspect + '_' + self.name + 'effector_001', dr=2)
        
        # rebuildCurve
        cmds.rebuildCurve(self.path_curve, constructionHistory=True, replaceOriginal=True, rebuildType=0, endKnots=1, keepRange=0, 
                            keepControlPoints=True, keepEndPoints=True, keepTangents=False, degree=3, tolerance=0.01)

        # create ik spline handle 
        path_handle = cmds.ikHandle(startJoint=self.path_skin_jnt_lit[0], endEffector=self.path_skin_jnt_lit[-1], curve=self.path_curve, 
                        sol='ikSplineSolver', ccv=False, scv=False, pcv=False, 
                        name=self.path_curve.replace('curve_', 'handle_'))
        # parent 
        cmds.parent(path_handle[0], self.rigNodesWorld)

        #cmds.rename(path_handle[-1], self.path_curve.replace('curve_', 'effector_'))
        # set advanced twist controls
        cmds.setAttr(path_handle[0] + '.dTwistControlEnable', 1)
        cmds.setAttr(path_handle[0] + '.dWorldUpType', 7)
        cmds.connectAttr(self.world_ctrl + '.worldMatrix[0]', path_handle[0] + '.dWorldUpMatrix')
        cmds.setAttr(path_handle[0] + '.rootOnCurve', 0)

        # set connect ikhandle attr
        # create remapValue
        remap_offset = cmds.createNode('remapValue', name='remap_' + self.aspect + '_' + self.name + 'IkHandleOffset_001')
        # set remapValue inputMax
        cmds.setAttr(remap_offset + '.inputMax', 100)

        # world ctrl connect remapValue inputValue
        cmds.connectAttr(self.world_offset, remap_offset + '.inputValue')
        #cmds.connectAttr(world_twist, path_handle[0] + '.twist')

        # remapValue outValue connect ikhandle attr
        cmds.connectAttr(remap_offset + '.outValue', path_handle[0] + '.offset')

        self.path_skin_jnt_lit.reverse()
        # create transform parentConstraint ik ctrl Follow Curve Animation
        for i, ii in zip(enumerate(self.spline_ik_skin_ctrl_lit), self.path_skin_jnt_lit):
            # create transform
            transform = cmds.createNode('transform', name='zero_PathAnimation_{:03d}'.format(i[0] + 1))
            # get ik ctrl translate rotate 
            translate = cmds.xform(i[1], query=True, translation=True, worldSpace=True)
            rotate = cmds.xform(i[1], query=True, rotation=True, worldSpace=True)
            # set ik ctrl translate rotate 
            cmds.xform(transform, translation=translate, worldSpace=True)
            cmds.xform(transform, rotation=rotate, worldSpace=True)
            # transaform parentConstraint ik ctrl 
            pc = cmds.parentConstraint(transform, i[1].replace('ctrl_', 'zero_'), weight=1)[0]
            # set parentConstraint interpType
            cmds.setAttr(pc + '.interpType', 2)
            # transform parent path bone 
            cmds.parent(transform, ii)

        # connect splineIkSkin rotate scale 
        self.connect_loc = self.spline_ik_skin_loc_lit[0].split('_')
        
        for i in self.interval_lit:
            cmds.connectAttr('ctrl_' + self.connect_loc[1] + '_' + self.connect_loc[2] + '_{:03d}.rotate'.format(i), self.connect_loc[0] + '_' + self.connect_loc[1] + '_' + self.connect_loc[2] + '_{:03d}.rotate'.format(i))
            cmds.connectAttr('ctrl_' + self.connect_loc[1] + '_' + self.connect_loc[2] + '_{:03d}.scale'.format(i), self.connect_loc[0] + '_' + self.connect_loc[1] + '_' + self.connect_loc[2] + '_{:03d}.scale'.format(i))

        for i in self.remove_interval_lit:
            cmds.connectAttr(self.connect_loc[0] + '_' + self.connect_loc[1] + '_' + self.connect_loc[2] + '_{:03d}.rotate'.format(i), 'driven_' + self.connect_loc[1] + '_' + self.connect_loc[2] + '_{:03d}.rotate'.format(i))
            # Scale locator connection SplineIkSKin controller
            spline_ik_skin_loc_split = self.spline_ik_skin_loc_lit[0].split('_')
            spline_ik_skin_ctrl_split = self.spline_ik_skin_ctrl_lit[0].split('_')
            spline_ik_skin_loc_name = spline_ik_skin_loc_split[0] + '_' + spline_ik_skin_loc_split[1] + '_' + spline_ik_skin_loc_split[2] + '_{:03d}'.format(i)
            spline_ik_skin_ctrl_name = 'connect_' + spline_ik_skin_ctrl_split[1] + '_' + spline_ik_skin_ctrl_split[2] + '_{:03d}'.format(i)
            cmds.connectAttr(spline_ik_skin_loc_name + '.scaleY', spline_ik_skin_ctrl_name + '.scaleY')
            cmds.connectAttr(spline_ik_skin_loc_name + '.scaleZ', spline_ik_skin_ctrl_name + '.scaleZ')

        path_ctrl_lit = []
        path_zero_lit = []
        # set path curve 
        path_curve_shape = cmds.listRelatives(self.path_curve, shapes=True)[0]
        cmds.setAttr(path_curve_shape + '.overrideEnabled', 1)
        cmds.setAttr(path_curve_shape + '.overrideDisplayType', 2)
        # path jnt and curve create SkinCluster
        cmds.skinCluster(path_jnt_lit, self.path_curve, toSelectedBones=True, maximumInfluences=1, 
                            name='skinCluster_' + self.aspect + '_' + self.name + 'PahtCuve_001')
                            
        # path grpup
        path_grp = cmds.createNode('transform', name='grp_' + self.aspect + '_' + self.name + 'PathCtrl_001')
        # create path curve ctrls
        for i in path_jnt_lit:
            # set jointOrient
            cmds.setAttr(i + '.jointOrient', 0, 0, 0)
            path_ctrl = cmds.curve(degree=1, point=offset, name=i.replace('jnt_', 'ctrl_'))
            cmds.rename(cmds.listRelatives(path_ctrl, shapes=True), i.replace('jnt_', 'ctrl_') + 'Shape')
            # set path ctrl scale 
            cmds.setAttr(path_ctrl + '.scale', self.wordl_fk_scale[0][0], self.wordl_fk_scale[0][1], self.wordl_fk_scale[0][2])
            path_ctrl_lit.append(path_ctrl)
            # get path skin jnt translate rotate 
            translate = cmds.xform(i, query=True, translation=True, worldSpace=True)
            rotate = cmds.xform(i, query=True, rotation=True, worldSpace=True)
            # set path skin jnt translate rotate 
            translate = cmds.xform(path_ctrl, translation=translate, worldSpace=True)
            rotate = cmds.xform(path_ctrl, rotation=rotate, worldSpace=True)
            # ctrl create zero
            path_zero = self.Hierarchical_group(path_ctrl)
            path_zero_lit.append(path_zero)
            # path zero parent path grp
            cmds.parent(path_zero, path_grp)
            # path jnt parent path ctrl 
            cmds.parent(i, path_ctrl)
            # hide path jnt 
            cmds.setAttr(i + '.visibility', 0)
            # set shapes color
            shapes = cmds.listRelatives(path_ctrl, shapes=True)[0]
            cmds.setAttr(shapes + '.overrideEnabled', 1)
            cmds.setAttr(shapes + '.overrideColor', 18)
            # Lock useless attributes
            for i in ['rotate', 'scale']:
                for ii in ['X', 'Y', 'Z']:
                    cmds.setAttr(path_ctrl + '.{}{}'.format(i, ii), lock=True, keyable=False, channelBox=False)
            cmds.setAttr(path_ctrl + '.visibility', lock=True, keyable=False, channelBox=False)
            
        # path_grp parent world ctrl
        cmds.parent(path_grp, self.world_ctrl)
        # set curve inheritsTransform
        cmds.setAttr(self.path_curve + '.inheritsTransform', 0)
        # path curve parent world
        cmds.parent(self.path_curve, self.world_ctrl)
        # world ctrl hide show
        cmds.connectAttr(self.world_path, path_grp + '.visibility')
        cmds.connectAttr(self.world_path, self.path_curve + '.visibility')

        path_bay_controller_lit = []
        # Interval controller related settings
        for i in path_ctrl_lit:
            # get shapes 
            shapes = cmds.listRelatives(i, shapes=True)[0]
            digit = path_ctrl_lit.index(i)
            if digit % 4 == 0:
                # set ctrl color 
                cmds.setAttr(shapes + '.overrideColor', 6)
                # get ctrl shapes point 
                point = cmds.ls(i + '.cv[*]', flatten=True)
                # get ctrl translate 
                translate = cmds.xform(i, query=True, translation=True, worldSpace=True)
                cmds.select(point)
                cmds.scale(2, 2, 2, relative=True, p=translate)
                cmds.select(clear=True)
                
                tail = i.split('_')[-1]
                
                path_bay_controller_lit.append(int(tail))        

        # Large controller constrains small controller
        for i in path_bay_controller_lit:
            seek = path_bay_controller_lit.index(i)
            
            head = i
            if i != path_bay_controller_lit[-1]:
                tail = path_bay_controller_lit[seek + 1]
            
            split = path_ctrl_lit[0].split('_')
            head_name = split[0] + '_' + split[1] + '_' + split[2] + '_{:03d}'.format(head)
            tail_name = split[0] + '_' + split[1] + '_' + split[2] + '_{:03d}'.format(tail)
            for ii in zip(range(head + 1, tail), [0.8, 0.5, 0.25]):
                constrained = 'driven_' + split[1] + '_' + split[2] + '_{:03d}'.format(ii[0])
                
                # create parentConstraint
                pc = cmds.parentConstraint(head_name, tail_name, constrained, maintainOffset=True, weight=1)[0]
                # set parentConstraint W0 W1
                cmds.setAttr(pc + '.w0', ii[1])
                cmds.setAttr(pc + '.w1', 1 - ii[1])

    def create_bone_sinScale(self, *args):
        world_ctrl_fatSpeed = self.world_ctrl + '.fatSpeed'
        world_ctrl_fat = self.world_ctrl + '.fat'
        world_ctrl_fatGo = self.world_ctrl + '.fatGo'
        world_ctrl_fatDelay = self.world_ctrl + '.fatDelay'

        # create a curve as a path animation
        cmds.addAttr(self.world_ctrl, longName='fatAttr', niceName='Fat Attr----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='fat', attributeType='float', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='fatSpeed', attributeType='float', defaultValue=2, keyable=True)
        cmds.addAttr(self.world_ctrl, longName='fatGo', attributeType='float', keyable=True)
        cmds.addAttr(self.world_ctrl, longName='fatDelay', attributeType='float', defaultValue=1.5, keyable=True)

        # set add attr 
        cmds.setAttr(self.world_ctrl + '.fatAttr', lock=True)
        cmds.setAttr(world_ctrl_fatDelay, keyable=False, channelBox=True)


        # create expression
        split_name = self.world_ctrl.split('_')
        exp_fat = 'exp_' + self.aspect + '_' + self.name + 'Fat_' + split_name[3]
        cmds.createNode('expression', name=exp_fat)

        # create fat expression string 
        string = ''
        for i in enumerate(self.sin_scale_jnt_lit):
            string += '{0}.scaleY={0}.scaleZ=sin(time*{1}+{2}+{3}*{4})*{5}+{6}+1;'.format(i[1], world_ctrl_fatSpeed, world_ctrl_fatGo, i[0], world_ctrl_fatDelay, world_ctrl_fat, world_ctrl_fat)
            string += '\n'

        # add expression string
        cmds.expression(exp_fat, edit=True, string=string, alwaysEvaluate=1, unitConversion='all')

    def create_body_waves_spine(self, *args):
        # copy spine ik curve
        wavesSpline_curve = cmds.duplicate(self.body_curve, name='curve_' + self.aspect + '_' + self.name + 'wavesSpline_001')[0]
        # create spline ikhandle
        wavesSpline_handle = cmds.ikHandle(startJoint=self.waveSpline_jnt_lit[0], endEffector=self.waveSpline_jnt_lit[-1], curve=wavesSpline_curve, 
                        sol='ikSplineSolver', ccv=False, scv=False, pcv=False, 
                        name=wavesSpline_curve.replace('curve_', 'handle_'))
        # effector rename 
        cmds.rename(wavesSpline_handle[-1], wavesSpline_curve.replace('curve_', 'effector_'))
        # parent 
        cmds.parent(wavesSpline_handle[0], self.rigNodesWorld)

        # self.waveSpline_jnt_lit pointConstraint self.wave_jnt_lit
        for i in zip(self.wave_ik_jnt_lit, self.wave_jnt_lit):
            cmds.pointConstraint(i[0], i[1], weight=1)

        # create spline bone 
        spline_jnt_lit = []
        spline_zero_lit = []
        for i in enumerate(zip(self.waveSpline_jnt_lit, self.fk_jnt_lit)):
            split_name = wavesSpline_curve.split('_')
            # create transfom
            transform = cmds.createNode('transform', name='zero_' + self.aspect + '_' + self.name + 'Path_{:03d}'.format(i[0] + 1))
            # hide transform
            cmds.setAttr(transform + '.visibility', 0)
            # create bone 
            jnt = cmds.createNode('joint', name='jnt_' + self.aspect + '_' + self.name + 'Path_{:03d}'.format(i[0] + 1), parent=transform)
            # set translate rotate 
            cmds.delete(cmds.parentConstraint(i[1][0], transform, weight=1))
            # trabsform parent fk ctrl
            cmds.parent(transform, i[1][1])
            
            
            spline_jnt_lit.append(jnt)
            spline_zero_lit.append(transform)


        # create skinCluster
        cmds.skinCluster(spline_jnt_lit, wavesSpline_curve, toSelectedBones=True, maximumInfluences=1, 
                            name=wavesSpline_curve.replace('curve_', 'skinCluster_'))

        # create waves spline ctrls 
        waves_spline_ctrl = cmds.curve(degree=1, point=Arrow2Way, name=wavesSpline_curve.replace('curve_', 'ctrl_'))
        # get shapes 
        waves_spline_ctrl_shape = cmds.listRelatives(waves_spline_ctrl, shapes=True)[0]
        # rename shapes
        waves_spline_ctrl_shape = cmds.rename(waves_spline_ctrl_shape, waves_spline_ctrl + 'Shape')

        # set Color 
        cmds.setAttr(waves_spline_ctrl_shape + '.overrideEnabled', 1)
        cmds.setAttr(waves_spline_ctrl_shape + '.overrideColor', 18)

        waves_spline_ctrl_loc_name = wavesSpline_curve.replace('curve_', 'loc_')
        waves_spline_ctrl_loc = cmds.createNode('locator', name=waves_spline_ctrl_loc_name + 'Shape')

        cmds.parent(waves_spline_ctrl_loc_name, self.spline_ik_skin_loc_grp)

        # ctrl parentConstraint loc and set 
        # ctrl connect loc scaleX scaleY
        cmds.connectAttr(waves_spline_ctrl + '.scaleY', waves_spline_ctrl_loc_name + '.scaleY') 
        cmds.connectAttr(waves_spline_ctrl + '.scaleZ', waves_spline_ctrl_loc_name + '.scaleZ') 

        # add attr
        cmds.addAttr(waves_spline_ctrl, longName='waveAttr', niceName='Wave Attr----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.addAttr(waves_spline_ctrl, longName='waveWidth', attributeType='float', min=0, defaultValue=12, keyable=True)
        cmds.addAttr(waves_spline_ctrl, longName='waveScale', attributeType='float', min=0, defaultValue=12, keyable=True)

        cmds.addAttr(waves_spline_ctrl, longName='stretchSwitch', niceName='Stretch Switch----------', attributeType='enum', enumName=' ', keyable=True)
        cmds.addAttr(waves_spline_ctrl, longName='stretch', attributeType='float', min=0, max=1, defaultValue=1, keyable=True)
        cmds.addAttr(waves_spline_ctrl, longName='follow', attributeType='long', min=0, max=1, defaultValue=1, keyable=True)
        cmds.addAttr(waves_spline_ctrl, longName='headFollow', attributeType='float', min=0, max=1, defaultValue=1, keyable=True)
        cmds.addAttr(waves_spline_ctrl, longName='headScaleFollow', attributeType='float', min=0, max=1, defaultValue=1, keyable=True)

        waves_spline_stretch = waves_spline_ctrl + '.stretch'
        waves_spline_follow = waves_spline_ctrl + '.follow'
        waves_spline_headFollow = waves_spline_ctrl + '.headFollow'
        waves_spline_headScaleFollow = waves_spline_ctrl + '.headScaleFollow'

        # lock attr 
        cmds.setAttr(waves_spline_ctrl + '.waveAttr', lock=True)
        cmds.setAttr(waves_spline_ctrl + '.stretchSwitch', lock=True)

        waves_spline_ctrl_waveWidth = waves_spline_ctrl + '.waveWidth'
        waves_spline_ctrl_waveScale = waves_spline_ctrl + '.waveScale'

        # set waves splone ctrl trans LinitX
        cmds.transformLimits(waves_spline_ctrl, translationX=[0, 0], enableTranslationX=[1, 0])
        # set ctrl scale 
        cmds.setAttr(waves_spline_ctrl + '.scale', self.wordl_fk_scale[0][0], self.wordl_fk_scale[0][1], self.wordl_fk_scale[0][2])
        # parent 
        cmds.parent(waves_spline_ctrl, self.fk_ctrl_lit[-1])
        # set translate and rotate 0, 0, 0
        cmds.setAttr(waves_spline_ctrl + '.translate', 0, 0, 0)
        cmds.setAttr(waves_spline_ctrl + '.rotate', 0, 0, 0)
        # set translate 
        cmds.setAttr(waves_spline_ctrl + '.translate', 10, 0, 0)
        # parent world
        cmds.parent(waves_spline_ctrl, world=True)
        # waves spline ctrl create zero group
        waves_spline_zero = self.Hierarchical_group(waves_spline_ctrl)[0]

        # waves spline attach to path locator
        waves_spline_motion_name = wavesSpline_curve.split('_')
        waves_spline_loc_name = 'loc_' + waves_spline_motion_name[1] + '_' + self.name + waves_spline_motion_name[2] + '_001'
        waves_spline_loc = cmds.createNode('locator', name=waves_spline_loc_name + 'Shape')
        # set tranlste 
        cmds.delete(cmds.parentConstraint(waves_spline_ctrl, waves_spline_loc_name, weight=1))

        # waves spline attach to motion path locator
        waves_spline_motion_loc_name = 'loc_' + waves_spline_motion_name[1] + '_' + self.name + waves_spline_motion_name[2] + 'Motion_001'
        waves_spline_motion_loc = cmds.createNode('locator', name=waves_spline_motion_loc_name + 'Shape')

        # create attach to motion path
        path = cmds.pathAnimation(waves_spline_motion_loc_name, self.path_curve, 
                    fractionMode=True, 
                    follow=True, 
                    followAxis='X', 
                    upAxis='y',
                    worldUpType='vector',
                    worldUpVector=[0, 1, 0],
                    inverseUp=False, 
                    inverseFront=False, 
                    bank=False,
                    startTimeU=0, 
                    endTimeU=1, 
                    name='motion_' + self.aspect + waves_spline_motion_name[2] + '_001'
                )

        # parentConstraint 
        pc = cmds.parentConstraint(waves_spline_motion_loc_name, waves_spline_zero, weight=1)[0]
        # set 
        cmds.setAttr(pc + '.interpType', 2)
        cmds.setAttr(waves_spline_zero + '.translate', 0, 0, 0)
        cmds.setAttr(waves_spline_zero + '.rotate', 0, 0, 0)
        # parent 
        cmds.parent(waves_spline_motion_loc_name, self.rigNodesWorld)
        cmds.parent(waves_spline_loc_name, self.rigNodesWorld)
        cmds.parent(waves_spline_zero, self.world_ctrl)
        # motion ctrl connect U Value
        # get waves spline shapes
        wavesSpline_curve_shape = cmds.listRelatives(self.path_curve, shapes=True)[0]
        # create node
        wavesSpline_curveInfo = cmds.createNode('curveInfo', name='curveInfo_' + waves_spline_motion_name[1] + '_' + waves_spline_motion_name[2] + '_001')
        wavesSpline_Divide = cmds.createNode('multiplyDivide', name='divide_' + waves_spline_motion_name[1] + '_' + waves_spline_motion_name[2] + '_001')
        wavesSpline_mult = cmds.createNode('multDoubleLinear', name='mult_' + waves_spline_motion_name[1] + '_' + waves_spline_motion_name[2] + '_001')
        wavesSpline_remap = cmds.createNode('remapValue', name='remap_' + waves_spline_motion_name[1] + '_' + waves_spline_motion_name[2] + '_001')
        wavesSpline_add = cmds.createNode('addDoubleLinear', name='add_' + waves_spline_motion_name[1] + '_' + waves_spline_motion_name[2] + '_001')
        wavesSpline_cond = cmds.createNode('condition', name='cond_' + waves_spline_motion_name[1] + '_' + waves_spline_motion_name[2] + '_001')
        wavesSpline_scale_mult = cmds.createNode('multDoubleLinear', name='mult_' + waves_spline_motion_name[1] + '_' + waves_spline_motion_name[2] + 'Scale_001')

        # set attr
        cmds.setAttr(wavesSpline_Divide + '.operation', 2)
        cmds.setAttr(wavesSpline_mult + '.input2', -1)
        cmds.setAttr(wavesSpline_remap + '.inputMax', 100)
        # connect attr
        cmds.connectAttr(wavesSpline_curve_shape + '.worldSpace[0]', wavesSpline_curveInfo + '.inputCurve')
        cmds.connectAttr(waves_spline_ctrl + '.translateX', wavesSpline_mult + '.input1')
        cmds.connectAttr(wavesSpline_curveInfo + '.arcLength', wavesSpline_Divide + '.input2X')
        cmds.connectAttr(wavesSpline_Divide + '.outputX', wavesSpline_add + '.input1')
        cmds.connectAttr(wavesSpline_add + '.output', wavesSpline_cond + '.colorIfTrueR')
        cmds.connectAttr(wavesSpline_Divide + '.outputX', wavesSpline_cond + '.colorIfFalseR')
        cmds.connectAttr(waves_spline_follow, wavesSpline_cond + '.firstTerm')
        cmds.connectAttr(waves_spline_ctrl + '.translateX', wavesSpline_scale_mult + '.input2')
        cmds.connectAttr(self.rigscale, wavesSpline_scale_mult + '.input1')
        cmds.connectAttr(wavesSpline_scale_mult + '.output', wavesSpline_Divide + '.input1X')
        cmds.connectAttr(wavesSpline_mult + '.output', waves_spline_ctrl.replace('ctrl_', 'space_') + '.translateX')
        cmds.connectAttr(self.world_ctrl + '.offset', wavesSpline_remap + '.inputValue')
        cmds.connectAttr(wavesSpline_remap + '.outValue', wavesSpline_add + '.input2')
        cmds.connectAttr(wavesSpline_cond + '.outColorR', path + '.uValue', force=True)

        # set cond attr 
        cmds.setAttr(wavesSpline_cond + '.secondTerm', 1)

        # scaleConstraint
        cmds.scaleConstraint(self.world_ctrl, waves_spline_ctrl.replace('ctrl_', 'driven_'))
        # Set waves_spline_ctrl  the position
        cmds.setAttr(waves_spline_ctrl + '.translateX', 16 * self.wordl_fk_scale[0][0])
        # ctrl pointConstraint  loc
        cmds.pointConstraint(waves_spline_ctrl, waves_spline_loc_name)
        # path curve tangent wavesSpline 
        cmds.tangentConstraint(self.path_curve, waves_spline_ctrl.replace('ctrl_', 'driven_'), 
                                    weight=1, aimVector=[1, 0, 0], upVector=[0, 1, 0], 
                                        worldUpType='objectrotation', worldUpVector=[0, 1, 0], worldUpObject=self.world_ctrl)


        fix_transfrom_lit = []
        fix_locator_lit = []
        for i in enumerate(zip(self.fk_jnt_lit, spline_jnt_lit)):
            split_name = i[1][0].split('_')
            # create transform grp 
            grp_name = 'grp_' + self.aspect + '_' + self.name + 'Fix_001'
            if not cmds.objExists(grp_name):
                cmds.createNode('transform', name=grp_name)
                pc = cmds.parentConstraint(self.world_ctrl, grp_name, weight=1)[0]
                cmds.parent(grp_name, self.rigNodesWorld)
                cmds.setAttr(pc + '.interpType', 2)
            # create transfom
            # create fix transform
            fix_name = 'transform_' + self.aspect + '_' + self.name + 'Fix_{:03d}'.format(i[0] + 1)
            # create fix locator
            fix_loc_name = 'loc_' + self.aspect + '_' + self.name + 'Fix_{:03d}'.format(i[0] + 1)
            
            cmds.createNode('transform', name=fix_name)
            cmds.createNode('locator', name=fix_loc_name, parent=fix_name)
            # set fix transform 
            cmds.delete(cmds.parentConstraint(i[1][1], fix_name, weight=1))
            cmds.pointConstraint(i[1][0], fix_name, weight=1, maintainOffset=True)
            
            cmds.parent(fix_name, grp_name)
            
            fix_transfrom_lit.append(fix_name)
            fix_locator_lit.append(fix_loc_name)

        # waves_spline_ctrl and fix locator pointConstraint path locator
        point_lit = []
        for i in zip(fix_transfrom_lit, spline_jnt_lit):
            point = cmds.pointConstraint(waves_spline_ctrl, i[0], i[1], maintainOffset=False, skip='x', weight=1)
            point_lit.append(point)

        # set constraint w0 w1 
        dist_node_lit = []
        for i in enumerate(zip(point_lit, fix_locator_lit)):
            # rename 
            split_name = fix_transfrom_lit[0].split('_')
            split_name = self.aspect + '_' + self.name + '_{:03d}'.format(i[0] + 1)
            # create node 
            dist_node = cmds.createNode('distanceBetween', name='dist_' + split_name)
            dist_node_lit.append(dist_node)
            remap_node = cmds.createNode('remapValue', name='remap_' + split_name)
            reve_node = cmds.createNode('reverse', name='reve_' + split_name)
            
            split_point1_name = 'divide_' + split_name[2] + 'PointOne_{:03d}'.format(i[0] + 1)
            split_point2_name = 'divide_' + split_name[2] + 'PointTwo_{:03d}'.format(i[0] + 1)
            divide_point1_node = cmds.createNode('multiplyDivide', name=split_point1_name)
            divide_point2_node = cmds.createNode('multiplyDivide', name=split_point2_name)
            
            
            # set node 
            cmds.setAttr(remap_node + '.inputMax', 0)
            cmds.setAttr(remap_node + '.outputMin', 1)
            cmds.setAttr(remap_node + '.outputMax', 0)
            cmds.setAttr(remap_node + '.value[0].value_FloatValue', 0)
            cmds.setAttr(remap_node + '.value[1].value_FloatValue', 1)
            cmds.setAttr(divide_point1_node + '.operation', 2)
            cmds.setAttr(divide_point2_node + '.operation', 2)
            
            # connect node 
            cmds.connectAttr(i[1][1] + '.worldPosition[0]', divide_point1_node + '.input1')
            waves_spline_motion_loc_shaoes = cmds.listRelatives(waves_spline_motion_loc_name, shapes=True)[0]
            cmds.connectAttr(waves_spline_motion_loc_shaoes + '.worldPosition[0]', divide_point2_node + '.input1')
            for pointOneTwo in [divide_point1_node, divide_point2_node]:
                for scaleXYZ in ['X', 'Y', 'Z']:
                    cmds.connectAttr(self.rigscale, pointOneTwo + '.input2' + scaleXYZ)
            
            
            cmds.connectAttr(divide_point1_node + '.output', dist_node + '.point1')
            cmds.connectAttr(divide_point2_node + '.output', dist_node + '.point2')
            cmds.connectAttr(waves_spline_ctrl_waveWidth, remap_node + '.inputMin')
            cmds.connectAttr(remap_node + '.outValue', reve_node + '.inputX')
            cmds.connectAttr(dist_node + '.distance', remap_node + '.inputValue')
            cmds.connectAttr(reve_node + '.outputX', i[1][0][0] + '.w0')
            cmds.connectAttr(remap_node + '.outValue', i[1][0][0] + '.w1')

        # hide waveSpline
        cmds.setAttr(self.waveSpline_jnt_lit[0] + '.visibility', 0)

        # wave bone parent fk ctrl 
        for i in zip(self.wave_jnt_lit, self.fk_jnt_lit):
            cmds.parent(i[0], i[1])

        # curve create nurbsSurface
        waves_surface_stretch = 'surface_' + self.aspect + '_' + self.name + 'WavesStretch_001'
        waves_curve_one = cmds.duplicate(self.body_curve, name='curve_' + self.aspect + '_' + self.name + 'WavesStretchDel_001')[0]
        waves_curve_two = cmds.duplicate(self.body_curve, name='curve_' + self.aspect + '_' + self.name + 'WavesStretchDel_002')[0]

        # Center waves curve point
        pivot = cmds.xform(self.world_ctrl, query=True, translation=True, worldSpace=True)
        cmds.setAttr(waves_curve_one + '.scalePivot', pivot[0], pivot[1], pivot[2])
        cmds.setAttr(waves_curve_one + '.rotatePivot', pivot[0], pivot[1], pivot[2])

        cmds.setAttr(waves_curve_two + '.scalePivot', pivot[0], pivot[1], pivot[2])
        cmds.setAttr(waves_curve_two + '.rotatePivot', pivot[0], pivot[1], pivot[2])

        # create locator pointConstraint after that displacement curve
        waves_curve_displacement_locator_name = 'loc_' + self.aspect + '_' + self.name + 'DisplacementWavesStretchDel_001'
        waves_curve_displacement_locator = cmds.createNode('locator', name= waves_curve_displacement_locator_name + 'Shape')
        cmds.parent(waves_curve_displacement_locator_name, self.world_ctrl)
        cmds.setAttr(waves_curve_displacement_locator_name + '.translate', 0, 0, 0)
        cmds.setAttr(waves_curve_displacement_locator_name + '.rotate', 0, 0, 0)
        pc = cmds.pointConstraint(waves_curve_displacement_locator_name, waves_curve_one)[0]

        # set waves curve one and two 
        cmds.setAttr(waves_curve_displacement_locator_name + '.translateY', 1)
        cmds.delete(pc)

        pc = cmds.pointConstraint(waves_curve_displacement_locator_name, waves_curve_two)[0]
        cmds.setAttr(waves_curve_displacement_locator_name + '.translateY', -1)
        cmds.delete(pc)

        self.nurbsSurface(waves_curve_one, waves_curve_two, waves_surface_stretch)
        # delect curve one and two
        cmds.delete(waves_curve_one, waves_curve_two, waves_curve_displacement_locator_name)

        # get waves_surface_stretch shapes
        waves_surface_stretch_shape = cmds.listRelatives(waves_surface_stretch, shapes=True)[0]

        # create foll group
        foll_grp = cmds.createNode('transform', name='grp_' + self.aspect + '_' + self.name + 'WavesStretchFoll_001')

        for i in enumerate(self.wave_stretch_jnt_lit):
            UV = self.get_UV(waves_surface_stretch_shape, i[1])
            foll = self.create_foll_setUV(i[0] + 1, waves_surface_stretch_shape, UV[0], UV[1], 'WavesStretch')
            cmds.parent(foll, foll_grp)
            
            # parentConstraint
            pc = cmds.parentConstraint(foll, i[1], mo=True, weight=1)[0]
            cmds.setAttr(pc + '.interpType', 2)

        stretch_parent_lit = []
        # stretch bone no stretch Fusion into ik bone
        for i in zip(self.waveSpline_jnt_lit, self.wave_stretch_jnt_lit, self.wave_ik_jnt_lit):
            pc = cmds.parentConstraint(i[0], i[1], i[2], weight=1)[0]
            cmds.setAttr(pc + '.interpType', 2)
            stretch_parent_lit.append(pc)

        # create skinCluster
        cmds.skinCluster(spline_jnt_lit, waves_surface_stretch, toSelectedBones=True, maximumInfluences=1, 
                            name='skinClust_' + self.aspect + '_' + self.name + 'WavesStretch_001')

        # create Stretch toggle button
        stretch_reverse = cmds.createNode('reverse', name='reve_' + self.aspect + '_' + self.name + 'Stretch_001')

        # connect 
        cmds.connectAttr(waves_spline_stretch, stretch_reverse + '.inputX')
        for i in stretch_parent_lit:
            cmds.connectAttr(stretch_reverse + '.outputX', i + '.w0')
            cmds.connectAttr(waves_spline_stretch, i + '.w1')

        # Set hierarchical relationships
        cmds.parent(foll_grp, self.rigNodesWorld)
        cmds.parent(waves_surface_stretch, self.rigNodesWorld)

        # set scale
        wave_scale_lit = [] 
        for i in self.wave_jnt_lit:
            pc = cmds.scaleConstraint(self.world_ctrl.replace('ctrl_', 'driven_'), waves_spline_ctrl_loc_name, i, offset=[1, 1, 1], skip='x', weight=1)[0]
            wave_scale_lit.append(pc)
            # hide wave jnt 
            cmds.setAttr(i + '.visibility', 0)

        # set Scale gradient
        for i in enumerate(zip(wave_scale_lit, fix_locator_lit, dist_node_lit)):
            # rename 
            split_name = fix_transfrom_lit[0].split('_')
            split_name_spline = self.aspect + '_' + self.name + 'Scale_{:03d}'.format(i[0] + 1)
            
            # create node 
            remap = cmds.createNode('remapValue', name='remap_' + split_name_spline)
            reve = cmds.createNode('reverse', name='reve_' + split_name_spline) 
            # connect 
            
            cmds.connectAttr(i[1][2] + '.distance', remap + '.inputValue')
            cmds.connectAttr(waves_spline_ctrl_waveScale, remap + '.inputMin')
            
            cmds.connectAttr(reve + '.outputX', i[1][0] + '.w0')
            
            cmds.connectAttr(remap + '.outValue', reve + '.inputX')
            cmds.connectAttr(remap + '.outValue', i[1][0] + '.w1')
            
            # set remapValue
            cmds.setAttr(remap + '.inputMax', 0)
            cmds.setAttr(remap + '.outputMin', 1)
            cmds.setAttr(remap + '.outputMax', 0)
            
            
            cmds.setAttr(remap + '.value[1].value_FloatValue', 0)
            cmds.setAttr(remap + '.value[0].value_FloatValue', 1)

        # set waves_spline_ctrl scale 
        cmds.setAttr(waves_spline_ctrl + '.scaleX', lock=True, keyable=False, channelBox=False)
        cmds.transformLimits(waves_spline_ctrl, scaleY=[0, 1], enableScaleY=[1, 0])
        cmds.transformLimits(waves_spline_ctrl, scaleZ=[0, 1], enableScaleZ=[1, 0])

        # set waves_spline_ctrl rotate 
        for XYZ in ['X', 'Y', 'Z']:
            cmds.setAttr(waves_spline_ctrl + '.rotate' + XYZ, lock=True, keyable=False, channelBox=False)

        # set waves_spline_ctrl follow offset
        # create locator
        waves_ctrl_follow_name = 'loc_' + self.aspect + '_' + self.name + 'wavesSplineFollow_001'
        waves_ctrl_follow = cmds.createNode('locator', name=waves_ctrl_follow_name + 'Shape')

        # create Attach to Motion Path
        path_Follow = cmds.pathAnimation(waves_ctrl_follow_name, self.path_curve, 
                    fractionMode=True, 
                    follow=True, 
                    followAxis='X', 
                    upAxis='y',
                    worldUpType='vector',
                    worldUpVector=[0, 1, 0],
                    inverseUp=False, 
                    inverseFront=False, 
                    bank=False,
                    startTimeU=0, 
                    endTimeU=1, 
                    name=waves_ctrl_follow_name.replace('loc_', 'motion_')
                )

        # connect 
        cmds.connectAttr(wavesSpline_remap + '.outValue', path_Follow + '.uValue', force=True)
        # waves_ctrl_follow_name pointConstraint self.path_skin_jnt_lit[-1]
        cmds.pointConstraint(waves_ctrl_follow_name, self.path_skin_jnt_lit[-1], weight=1, maintainOffset=True)

        cmds.parent(waves_ctrl_follow_name, self.rigNodesWorld)

        # self.hind_jnt_lit RotateX connect self.Skin_jnt_lit RotateX
        for i in zip(self.hind_jnt_lit, self.Skin_jnt_lit):
            cmds.connectAttr(i[0] + '.rotateX', i[1] + '.rotateX')

        hind_plus_name_lit = []
        # Merge scaled bones onto skin bones
        for i in enumerate(zip(self.hind_jnt_lit, self.sin_scale_jnt_lit, self.wave_jnt_lit, self.Skin_jnt_lit)):
            hind_plus_name = 'plus_' + self.aspect + self.name + 'FusionHind_{:03d}'.format(i[0] + 1)
            wave_plus_name = 'plus_' + self.aspect + self.name + 'FusionWave_{:03d}'.format(i[0] + 1)
            scale_plus_name = 'plus_' + self.aspect + self.name + 'FusionScale_{:03d}'.format(i[0] + 1)
            
            # create node 
            cmds.createNode('plusMinusAverage', name=hind_plus_name) 
            cmds.createNode('plusMinusAverage', name=wave_plus_name)
            cmds.createNode('plusMinusAverage', name=scale_plus_name)
            
            hind_plus_name_lit.append(hind_plus_name)
            
            # set node attr
            for XYZ in ['Y', 'Z']:
                # node attr connect 
                cmds.connectAttr(i[1][0] + '.scale' + XYZ, hind_plus_name + '.input3D[0].input3D' + XYZ.lower())
                cmds.connectAttr(i[1][2] + '.scale' + XYZ, wave_plus_name + '.input3D[0].input3D' + XYZ.lower())
                cmds.connectAttr(i[1][1] + '.scale' + XYZ, scale_plus_name + '.input3D[0].input3D' + XYZ.lower())
                
                cmds.connectAttr(wave_plus_name + '.output3D.output3D' + XYZ.lower(), hind_plus_name + '.input3D[1].input3D' + XYZ.lower())
                cmds.connectAttr(scale_plus_name + '.output3D.output3D' + XYZ.lower(), hind_plus_name + '.input3D[2].input3D' + XYZ.lower())
                
                cmds.connectAttr(hind_plus_name + '.output3D.output3D' + XYZ.lower(), i[1][3] + '.scale' + XYZ)
                
                # set plusMinusAverage attr 
                cmds.setAttr(wave_plus_name + '.input3D[1].input3D' + XYZ.lower(), -1)
                cmds.setAttr(scale_plus_name + '.input3D[1].input3D' + XYZ.lower(), -1)

        # self.wave_ik_jnt_lit pointConstraint skin bone 
        for i in zip(self.wave_ik_jnt_lit, self.Skin_jnt_lit):
            cmds.pointConstraint(i[0], i[1], offset=[0, 0, 0], weight=1)


        for ii in self.remove_interval_lit:
            # spline ik skin ctrl add scale 
            spline_ik_skin_ctrl_interval = cmds.createNode('plusMinusAverage', name='plus__' + self.aspect + '_' + self.name + 'SplineIkCtrlScaleAdd_{:03d}'.format(ii))
                
            spline_ik_skin_ctrl_name = 'ctrl_' + self.connect_loc[1] + '_' + self.connect_loc[2] + '_{:03d}'.format(ii)
            cmds.connectAttr(hind_plus_name_lit[ii - 1] + '.output3D.output3Dy', spline_ik_skin_ctrl_interval + '.input3D[0].input3Dy')
            cmds.connectAttr(hind_plus_name_lit[ii - 1] + '.output3D.output3Dz', spline_ik_skin_ctrl_interval + '.input3D[0].input3Dz')
                
            cmds.connectAttr(spline_ik_skin_ctrl_name + '.scaleY', spline_ik_skin_ctrl_interval + '.input3D[1].input3Dy')
            cmds.connectAttr(spline_ik_skin_ctrl_name + '.scaleZ', spline_ik_skin_ctrl_interval + '.input3D[1].input3Dz')
                
            cmds.setAttr(spline_ik_skin_ctrl_interval + '.input3D[2].input3Dy', -1)
            cmds.setAttr(spline_ik_skin_ctrl_interval + '.input3D[2].input3Dz', -1)
                
            cmds.connectAttr(spline_ik_skin_ctrl_interval + '.output3D.output3Dy', self.Skin_jnt_lit[ii - 1] + '.scaleY', force=True)
            cmds.connectAttr(spline_ik_skin_ctrl_interval + '.output3D.output3Dz', self.Skin_jnt_lit[ii - 1]  + '.scaleZ', force=True)

        # Scaling is integrated into the scaling of the neck and head
        fk_ctrl_driven = self.fk_ctrl_lit[0].replace('ctrl_', 'driven_')
        fk_ctrl_split = fk_ctrl_driven.split('_')

        # create node 
        fk_ctrl_remapY = cmds.createNode('remapValue', name='remap_' + self.aspect + fk_ctrl_split[2] + 'HeadScaleFollowY_001')
        fk_ctrl_remapZ = cmds.createNode('remapValue', name='remap_' + self.aspect + fk_ctrl_split[2] + 'HeadScaleFollowZ_001')

        # set node 
        cmds.setAttr(fk_ctrl_remapY + '.outputMin', 1)
        cmds.setAttr(fk_ctrl_remapZ + '.outputMin', 1)

        # set self.world_ctrl, self.Skin_jnt_lit[0], self.fk_ctrl_lit[0] connect 
        headFollow = cmds.pointConstraint(self.fk_ctrl_lit[0].replace('ctrl_', 'zero_'), self.Skin_jnt_lit[0], self.fk_ctrl_lit[0].replace('ctrl_', 'driven_'), maintainOffset=True, weight=1)[0]
        cmds.connectAttr(self.Skin_jnt_lit[0] + '.scaleY', fk_ctrl_remapY + '.outputMax')
        cmds.connectAttr(self.Skin_jnt_lit[0] + '.scaleZ', fk_ctrl_remapZ + '.outputMax')

        cmds.connectAttr(waves_spline_headScaleFollow, fk_ctrl_remapY + '.inputValue')
        cmds.connectAttr(waves_spline_headScaleFollow, fk_ctrl_remapZ + '.inputValue')


        cmds.connectAttr(fk_ctrl_remapY + '.outValue', self.fk_ctrl_lit[0].replace('ctrl_', 'connect_') + '.scaleY')
        cmds.connectAttr(fk_ctrl_remapZ + '.outValue', self.fk_ctrl_lit[0].replace('ctrl_', 'connect_') + '.scaleZ')

        waves_spline_headScaleFollow

        # create node 
        headFollow_reve = cmds.createNode('reverse', name='rev_' + self.aspect + '_' + self.name + 'wavesSplineHeadFollow_001')

        cmds.connectAttr(headFollow_reve + '.outputX', headFollow + '.w0')
        cmds.connectAttr(waves_spline_headFollow, headFollow + '.w1')
        cmds.connectAttr(waves_spline_headFollow, headFollow_reve + '.inputX')

        # set translate rotate
        cmds.delete(cmds.parentConstraint(waves_spline_ctrl, waves_spline_ctrl_loc_name, weight=1))

        for i in zip(self.fk_ctrl_lit[1:], self.new_snakebody_neck_bone_lit[1:-1]):
            connect = self.fk_ctrl_lit[0].replace('ctrl_', 'connect_')
            # create node 
            fk_ctrl_plus = cmds.createNode('plusMinusAverage', name=i[0].replace('ctrl_', 'plus_'))
            
            # node attr connect 
            cmds.connectAttr(i[0] + '.scale', fk_ctrl_plus + '.input3D[0]')
            cmds.connectAttr(connect + '.scale', fk_ctrl_plus + '.input3D[1]')
            cmds.connectAttr(fk_ctrl_plus + '.output3D', i[1] + '.scale', force=True)


            # set node attr 
            cmds.setAttr(fk_ctrl_plus + '.input3D[2].input3Dx', -1)
            cmds.setAttr(fk_ctrl_plus + '.input3D[2].input3Dy', -1)
            cmds.setAttr(fk_ctrl_plus + '.input3D[2].input3Dz', -1)

        # Locking attributes to prevent accidental contact
        for i in self.new_snakebody_neck_bone_lit:
            cmds.setAttr(i + '.translate', lock=True)
            cmds.setAttr(i + '.rotate', lock=True)
            cmds.setAttr(i + '.scale', lock=True)
            cmds.setAttr(i + '.visibility', lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i + '.radius', lock=True, keyable=False, channelBox=False)

        # Set goal constraints, rotate to maintain form
        for i in enumerate(zip(self.fk_jnt_lit, self.Skin_jnt_lit)):
            try:
                one = self.Skin_jnt_lit[i[0]]
                two = self.Skin_jnt_lit[i[0] + 1]
                cmds.aimConstraint(two, one, offset=[0, 0, 0], weight=1, aimVector=[1, 0, 0], upVector=[0, 1, 0], 
                                        worldUpType='objectrotation', worldUpVector=[0, 1, 0], 
                                            worldUpObject=i[1][0], skip='x')
            except:
                pass
        # Locking attributes to prevent accidental contact
        for i in self.Skin_jnt_lit:
            # hide lock skin bone  visibility and radius
            cmds.setAttr(i + '.visibility', lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i + '.radius', lock=True, keyable=False, channelBox=False)
            # lock attr Preventing accidental contact
            cmds.setAttr(i + '.translate', lock=True)
            cmds.setAttr(i + '.rotate', lock=True)
            cmds.setAttr(i + '.scale', lock=True)

        # Place the bones that need to be hidden into the hidden group
        cmds.parent(self.constraint_jnt_lit[0], self.hideJnt_zero)
        cmds.parent(self.path_skin_jnt_lit[-1], self.hideJnt_zero)
        cmds.parent(self.waveSpline_jnt_lit[0], self.hideJnt_zero)
        cmds.parent(self.wave_stretch_jnt_lit[0], self.hideJnt_zero)
        cmds.parent(self.wave_ik_jnt_lit[0], self.hideJnt_zero)
        cmds.parent(self.spline_ik_jnt_lit[0], self.hideJnt_zero)

        cmds.select(clear=True)


        ############################### set body ikHandle Advanced Twist Controls ###############################
        body_ikHandle_worldUpObject_ctrl_transform = 'ctrl_' + self.aspect + '_' + self.name + 'BodyWorldUpObject_001'
        cmds.curve(degree=1, point=Pyramid, name=body_ikHandle_worldUpObject_ctrl_transform)
        body_ikHandle_worldUpObject_ctrl_shape = cmds.rename(cmds.listRelatives(body_ikHandle_worldUpObject_ctrl_transform, shapes=True)[0], 
                                                                body_ikHandle_worldUpObject_ctrl_transform + 'Shape')
        # set ctrl scale 
        cmds.setAttr(body_ikHandle_worldUpObject_ctrl_transform + '.scale', 
                        self.wordl_fk_scale[0][0], self.wordl_fk_scale[0][1], self.wordl_fk_scale[0][2])
        # set Color 
        cmds.setAttr(body_ikHandle_worldUpObject_ctrl_shape + '.overrideEnabled', 1)
        cmds.setAttr(body_ikHandle_worldUpObject_ctrl_shape + '.overrideColor', 14)
        # set body_ikHandle_worldUpObject2_ctrl_transform
        cmds.delete(cmds.parentConstraint(self.Skin_jnt_lit[-1], body_ikHandle_worldUpObject_ctrl_transform, weight=1))
        body_ikHandle_worldUpObject_ctrl_zero = self.Hierarchical_group(body_ikHandle_worldUpObject_ctrl_transform)


        # open Enable Twist Controls
        cmds.setAttr(self.ik_spline_handle[0] + '.dTwistControlEnable', 1)
        # se ikHandle World Up Type 
        cmds.setAttr(self.ik_spline_handle[0] + '.dWorldUpType', 4)


        # create World Up Object locator
        neck_ikHandle_worldUpObject_zero_transform = 'zero_' + self.aspect + '_' + self.name + 'NeckWorldUpObject_001'
        neck_ikHandle_worldUpObject_loc_transform = 'loc_' + self.aspect + '_' + self.name + 'NeckWorldUpObject_001'
        cmds.createNode('transform', name=neck_ikHandle_worldUpObject_zero_transform)
        cmds.createNode('locator', name=neck_ikHandle_worldUpObject_loc_transform + 'Shape')
        cmds.parent(neck_ikHandle_worldUpObject_loc_transform, neck_ikHandle_worldUpObject_zero_transform)
        # create World Up Object2 locator
        body_ikHandle_worldUpObject2_zero_transform = 'zero_' + self.aspect + '_' + self.name + 'BodyWorldUpObject2_001'
        body_ikHandle_worldUpObject2_loc_transform = 'loc_' + self.aspect + '_' + self.name + 'BodyWorldUpObject2_001'
        cmds.createNode('transform', name=body_ikHandle_worldUpObject2_zero_transform)
        cmds.createNode('locator', name=body_ikHandle_worldUpObject2_loc_transform + 'Shape')
        cmds.parent(body_ikHandle_worldUpObject2_loc_transform, body_ikHandle_worldUpObject2_zero_transform)

        #World Up Object locator
        cmds.delete(cmds.parentConstraint(self.fk_ctrl_lit[1], neck_ikHandle_worldUpObject_zero_transform, weight=1))
        cmds.delete(cmds.parentConstraint(self.Skin_jnt_lit[-1], body_ikHandle_worldUpObject2_zero_transform, weight=1))

        cmds.connectAttr(self.fk_ctrl_lit[1] + '.rotateX', neck_ikHandle_worldUpObject_loc_transform + '.rotateX')
        cmds.connectAttr(body_ikHandle_worldUpObject_ctrl_transform + '.rotateX', body_ikHandle_worldUpObject2_loc_transform + '.rotateX')

        # locator connect World Up Object
        cmds.connectAttr(neck_ikHandle_worldUpObject_loc_transform + '.worldMatrix[0]', self.ik_spline_handle[0] + '.dWorldUpMatrix')
        cmds.connectAttr(body_ikHandle_worldUpObject2_loc_transform + '.worldMatrix[0]', self.ik_spline_handle[0] + '.dWorldUpMatrixEnd')

        # lock body_ikHandle_worldUpObject_ctrl_transform Useless attribute
        for i in ['translate', 'rotate', 'scale']:
            for ii in ['X', 'Y', 'Z']:
                cmds.setAttr(body_ikHandle_worldUpObject_ctrl_transform + '.' + i + ii, 
                                lock=True, keyable=False, channelBox=False)

        cmds.setAttr(body_ikHandle_worldUpObject_ctrl_transform + '.visibility', 
                        lock=True, keyable=False, channelBox=False)
        cmds.setAttr(body_ikHandle_worldUpObject_ctrl_transform + '.rotateX', 
                        lock=False, keyable=True, channelBox=False)

        cmds.parent([neck_ikHandle_worldUpObject_zero_transform, body_ikHandle_worldUpObject2_zero_transform], self.rigNodesLocal)
        cmds.parent(body_ikHandle_worldUpObject_ctrl_zero, self.spline_ik_skin_ctrl_lit[-1])

        # delete Excess objects
        cmds.delete(self.body_curve, self.body_jnt_lit[0])

        # Create a sets to store all objects that need to be quickly selected
        cmds.sets(self.Distr_Node_Set, self.Skin_Bone_Set, name='set_' + self.aspect + '_' + self.name + '_Root')
        
    def Manual_Adjustment_Create_Joint(self, *args):
        self.create_master()
        judgement = cmds.checkBox('manual_adjustment', query=True, value=True)
        
        if judgement:
            self.create_joints()
            self.adjust_create_joint()
            self.Number_enable_False()
        else:
            self.create_joints()
            self.Number_enable_False()
        
    def run(self, *args):
        self.create_neck_bone_ctrl()
        self.create_body_ik_fk()
        self.create_creep_function()
        self.create_path_curve_animation()
        self.create_bone_sinScale()
        self.create_body_waves_spine()
        cmds.button('Run', edit=True, enable=False)

execute = snake()
execute.tool_ui()
