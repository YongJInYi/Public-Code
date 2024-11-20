import maya.cmds as cmds 
import re

class FK_TO_IK():
    def __init__(self):
        #------------------------------------------------------------------------------------------#
        if cmds.window("ik_fk_seamless_switching", exists=True):
            cmds.window('ik_fk_seamless_switching', edit=True, sizeable=False, widthHeight=[312, 415])
            cmds.deleteUI("ik_fk_seamless_switching")
        
        window = cmds.window('ik_fk_seamless_switching', 
                                widthHeight=[312, 415], 
                                title='Ik Fk Seamless Switching', 
                                iconName='Ik Fk Seamless Switching', 
                                sizeable=False, 
                                menuBar=True)
        
        ##########################################################
        cmds.rowColumnLayout(numberOfRows=9)# Ui
        
        #FK ctrl
        cmds.rowColumnLayout( numberOfRows=1)#2
        cmds.text('                 Pos:     ')
        cmds.text('             Start:     ')
        cmds.text('             End:')
        cmds.setParent( '..' )#2
        
        cmds.rowColumnLayout( numberOfRows=1)#1
        cmds.text('Set Time:')
        set_time_notes_v1 = 'Pos is the number of frames set as the default state'
        cmds.floatFieldGrp("set_time", numberOfFields=3, value=[0.0,0.0,0,0], precision=3, annotation=set_time_notes_v1)
        
        self.Refresh()

        cmds.popupMenu()
        cmds.menuItem('Refresh_time', label='Refresh Time', command=self.Refresh)
        cmds.setParent( '..' )#1
        
        cmds.separator(h=5)
        
        # Mirror Configuration
        cmds.rowColumnLayout(numberOfRows=1) #Mirror
        
        cmds.rowColumnLayout( numberOfRows=1) # ui2
        animation_notes = 'Turn on animation switching'
        cmds.checkBox('Animation', label='Animation', value=False, annotation=animation_notes)
        cmds.setParent( '..' )# Ui2
        
        mirror_notes = 'Enable Mirror Switching'
        cmds.checkBox('Mirror', label='Mirror', value=False, changeCommand=self.on_off_mirror_butt, annotation=mirror_notes)
        
        mirror_replace_one_notes = 'String before replacement'
        cmds.textField('mirror_replace_one', text='LfLeg_', width=85, editable=False, annotation=mirror_replace_one_notes)
        
        mirror_replace_two_notes = 'String After replacement'
        cmds.textField('mirror_replace_two', text='RtLeg_', width=85, editable=False, annotation=mirror_replace_two_notes)
        
        cmds.setParent( '..' ) #Mirror

        cmds.separator(h=5)
        
        cmds.rowColumnLayout( numberOfRows=1) # ui1
        # set fps ui
        fps_notes = 'Set fps for animation playback'
        cmds.optionMenu('FPS', label='FPS:', changeCommand=self.fps, highlightColor=[0, 0.5, 1], visibleChangeCommand=self.fps, width=290, 
                            annotation=fps_notes)
        cmds.menuItem(label='15fps')
        cmds.menuItem(label='24fps')
        cmds.menuItem(label='25fps')
        cmds.menuItem(label='30fps')
        cmds.menuItem(label='48fps')
        cmds.menuItem(label='50fps')
        cmds.menuItem(label='60fps')
        # select Initial Position
        cmds.optionMenu('FPS', edit=True, select=4)
        cmds.setParent( '..' )# ui1
        
        cmds.helpLine()
        
        cmds.separator(h=5)
        
        cmds.setParent( '..' )# Ui
        ##########################################################

        form = cmds.formLayout()
        tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        cmds.formLayout(form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
        
        child1 = cmds.rowColumnLayout(numberOfColumns=2) #child1
        
        #########################
        cmds.rowColumnLayout( numberOfRows=4)# ###
        cmds.frameLayout(l='Fk-Ctrl', cll=False, backgroundColor=[0, 0.2, 0.4], width=300) # frameLayout2

        cmds.popupMenu()
        cmds.menuItem('get_all_fk_controller', label='Get All Fk Controller', command=self.get_fk_all_controller)
        cmds.menuItem('ik_transfer_fk', label='Transfer >>>>', command=self.ik_transfer_fk)

        cmds.rowColumnLayout( numberOfRows=1)
        ik_crotch_shoulder = 'Place the fk crotch or shoulder joint controller here'
        cmds.textField('pickup_location_one', text='', w=185, editable=True, annotation=ik_crotch_shoulder)
        cmds.button( label='Crotch \ Shoulder', width=100, command=self.get_fk_one, annotation=ik_crotch_shoulder)
        cmds.setParent( '..' )

        cmds.rowColumnLayout( numberOfRows=1)
        ik_knee_elbow = 'Place the fk knee or elbow joint controller here'
        cmds.textField('pickup_location_two', text='', w=185, editable=True, annotation=ik_knee_elbow)
        cmds.button( label='Knee \ Elbow', width=100, command=self.get_fk_two, annotation=ik_knee_elbow)
        cmds.setParent( '..' )

        cmds.rowColumnLayout( numberOfRows=1)
        ik_ankle_wrist = 'Place the fk ankle or wrist joint controller here'
        cmds.textField('pickup_location_three', text='', w=185, editable=True, annotation=ik_ankle_wrist)
        cmds.button( label='Ankle \ Wrist', width=100, command=self.get_fk_three, annotation=ik_ankle_wrist)
        cmds.setParent( '..' )
        cmds.setParent( '..' )
        #------------------#iK ctrl#------------------#
        cmds.frameLayout(l='Ik-Ctrl', cll=False, backgroundColor=[0.25, 0, 0], width=300)

        cmds.popupMenu()
        cmds.menuItem('get_all_ik_controller', label='Get All Ik Controller', command=self.get_ik_all_controller)

        cmds.rowColumnLayout( numberOfRows=1)#
        ik_polar_vector = 'Place the Ik pole vector controller here'
        cmds.textField('pickup_Polar_vector', text='', width=185, editable=True, annotation=ik_polar_vector)
        cmds.button( label='Polar vector', width=100, command=self.get_ik_one, annotation=ik_polar_vector)
        cmds.setParent( '..' )#
        
        cmds.rowColumnLayout( numberOfRows=1)#
        ik_ankle_wrist = 'Place the controller for Ik here'
        cmds.textField('pickup_controller', text='', w=185, editable=True, annotation=ik_ankle_wrist)
        cmds.button( label='Ankle \ wrist', width=100, command=self.get_ik_two, annotation=ik_ankle_wrist)
        cmds.setParent( '..' )#
        
        cmds.rowColumnLayout( numberOfRows=1, enable=False)#
        ik_make_up_the_number = 'This is a useless decoration'
        cmds.textField('make_up_the_number', text='make up the number', w=185, editable=False, annotation=ik_make_up_the_number)
        cmds.button( label='', width=100, command=self.get_ik_two, annotation=ik_make_up_the_number)
        cmds.setParent( '..' )#
        
        cmds.separator(h=1)
        
        ik_run_txt = 'After setting, click on "Run"'
        cmds.button(label='Run', width=220, command=self.single_frame, annotation=ik_run_txt)
        
        cmds.setParent( '..' )  # frameLayout2
        
        cmds.setParent( '..' )
        ##########################
        cmds.setParent( '..' ) #child1
        
        child2 = cmds.rowColumnLayout(numberOfColumns=2)# child2
        ##########################################################################
        #FK ctrl
        #------------------fk controller------------------#
        cmds.rowColumnLayout( numberOfRows=4)# ###
        
        cmds.frameLayout(l='Fk-Ctrl', cll=False, backgroundColor=[0, 0.2, 0.4], width=300)
        cmds.popupMenu()
        cmds.menuItem('get_all_fk_controller', label='Get All Fk Controller', command=self.get_ik_to_fk_fk_all_controller)
        cmds.menuItem('fk_transfer_ik', label='<<<< Transfer', command=self.fk_transfer_ik)

        cmds.rowColumnLayout( numberOfRows=1)
        fk_crotch_shoulder = 'Place the fk Crotch or Shoulder joint controller here'
        cmds.textField('fk_crotch_shoulder_ctrl', text='', width=185, annotation=fk_crotch_shoulder)
        cmds.button( label='Crotch \ Shoulder', width=100, command=self.get_ik_ctrl_one, annotation=fk_crotch_shoulder)
        cmds.setParent( '..' )
        ''
        cmds.rowColumnLayout( numberOfRows=1)
        fk_knee_elbow = 'Place the ik Knee or Elbow joint Controller here'
        cmds.textField('fk_Knee_elbow_ctrl', text='', width=185, annotation=fk_knee_elbow)
        cmds.button( label='Knee \ Elbow', width=100, command=self.get_ik_ctrl_two, annotation=fk_knee_elbow)
        cmds.setParent( '..' )

        cmds.rowColumnLayout( numberOfRows=1)
        fk_ankle_wrist = 'Place the ik Ankle or Wrist joint Controller here'
        cmds.textField('fk_Ankle_wrist_ctrl', text='', width=185, annotation=fk_ankle_wrist)
        cmds.button( label='Ankle \ Wrist', width=100, command=self.get_ik_ctrl_three, annotation=fk_ankle_wrist)
        cmds.setParent( '..' )
        
        cmds.setParent( '..' )# ###
        #------------------iK joint------------------#
        cmds.frameLayout(l='Ik-Joint', cll=False, backgroundColor=[0.25, 0, 0], width=300)
        cmds.popupMenu()
        cmds.menuItem('get_all_fk_controller', label='Get All Fk Controller', command=self.get_ik_to_fk_fk_all_bone)
        
        cmds.rowColumnLayout( numberOfRows=1)
        fk_crotch_shoulder_bone = 'Place the ik Crotch or Shoulder joint Bone here'
        cmds.textField('ik_crotch_shoulder_joint', text='', w=185, annotation=fk_crotch_shoulder_bone)
        cmds.button( label='Crotch \ Shoulder', width=100, command=self.get_ik_bone_one, annotation=fk_crotch_shoulder_bone)
        cmds.setParent( '..' )

        cmds.rowColumnLayout( numberOfRows=1)
        fk_knee_elbow_bone = 'Place the ik Knee or Elbow joint Bone here'
        cmds.textField('ik_Knee_elbow_joint', text='', width=185, annotation=fk_knee_elbow_bone)
        cmds.button( label='Knee \ Elbow', width=100, command=self.get_ik_bone_two, annotation=fk_knee_elbow_bone)
        cmds.setParent( '..' )

        cmds.rowColumnLayout( numberOfRows=1)
        fk_ankle_wrist_bone = 'Place the ik Ankle or Wrist joint Bone here'
        cmds.textField('ik_Ankle_wrist_joint', text='', width=185, annotation=fk_ankle_wrist_bone)
        cmds.button( label='Ankle \ Wrist', width=100, command=self.get_ik_bone_three, annotation=fk_ankle_wrist_bone)
        cmds.setParent( '..' )
        
        cmds.separator(h=1)

        fk_run_txt = 'After setting, click on "Run" --- Ik Fk Switches To IK Mode'
        cmds.button(label='Run', width=220, command=self.run_ik_to_fk, annotation=fk_run_txt)
        
        cmds.setParent( '..' )# child2
        ##########################################################################
        cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Ik'), (child2, 'Fk')) )
        cmds.showWindow(window)
        cmds.window('ik_fk_seamless_switching', edit=True, widthHeight=[312, 415])
    ###############################################################################
    
    
    
    ##########################################################################################
    def fps(self, name):
        cmds.currentUnit(time=name)
    
    def on_off_mirror_butt(self, *args):
        Mirror = cmds.checkBox('Mirror', query=True, value=True)
        cmds.textField('mirror_replace_one', edit=True, editable=Mirror)
        cmds.textField('mirror_replace_two', edit=True, editable=Mirror)
    
    def delete_node(self, *args):
        cmds.delete(self.locator_lit)
    
    ##########################################################################################
    def get_ik_one(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("pickup_Polar_vector",  edit=True, text=sel[0])
        
    def get_ik_two(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("pickup_controller",  edit=True, text=sel[0])
    
    def get_fk_one(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("pickup_location_one",  edit=True, text=sel[0])
        
    def get_fk_two(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("pickup_location_two",  edit=True, text=sel[0])
        
    def get_fk_three(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("pickup_location_three",  edit=True, text=sel[0])
            
    #---------------------------------------------------------------------------
    def get_ik_ctrl_one(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("fk_crotch_shoulder_ctrl",  edit=True, text=sel[0])
        
    def get_ik_ctrl_two(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("fk_Knee_elbow_ctrl",  edit=True, text=sel[0])
        
    def get_ik_ctrl_three(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("fk_Ankle_wrist_ctrl",  edit=True, text=sel[0])
    #---------------------------------------------------------------------------
    def get_ik_bone_one(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("ik_crotch_shoulder_joint",  edit=True, text=sel[0])
        
    def get_ik_bone_two(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("ik_Knee_elbow_joint",  edit=True, text=sel[0])
        
    def get_ik_bone_three(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textField("ik_Ankle_wrist_joint",  edit=True, text=sel[0])
    ##########################################################################################
    
    ##########################################################################################
    def get_ik_all_controller(self, *args):
        sel = cmds.ls(selection=True)
        if len(sel) == 2:
            cmds.textField("pickup_Polar_vector",  edit=True, text=sel[0])
            cmds.textField("pickup_controller",  edit=True, text=sel[1])
    
    def get_fk_all_controller(self, *args):
        sel = cmds.ls(selection=True)
        if len(sel) == 3:
            cmds.textField("pickup_location_one",  edit=True, text=sel[0])
            cmds.textField("pickup_location_two",  edit=True, text=sel[1])
            cmds.textField("pickup_location_three",  edit=True, text=sel[2])
    
    def get_ik_to_fk_fk_all_controller(self, *args):
        sel = cmds.ls(selection=True)
        if len(sel) == 3:
            cmds.textField("fk_crotch_shoulder_ctrl",  edit=True, text=sel[0])
            cmds.textField("fk_Knee_elbow_ctrl",  edit=True, text=sel[1])
            cmds.textField("fk_Ankle_wrist_ctrl",  edit=True, text=sel[2])
            
    def get_ik_to_fk_fk_all_bone(self, *args):
        sel = cmds.ls(selection=True)
        if len(sel) == 3:
            cmds.textField("ik_crotch_shoulder_joint",  edit=True, text=sel[0])
            cmds.textField("ik_Knee_elbow_joint",  edit=True, text=sel[1])
            cmds.textField("ik_Ankle_wrist_joint",  edit=True, text=sel[2])
    ##########################################################################################
            
    ##########################################################################################
    def ik_transfer_fk(self, *args):
        # get attr 
        one = cmds.textField("pickup_location_one",  query=True, text=True)
        two = cmds.textField("pickup_location_two",  query=True, text=True)
        three = cmds.textField("pickup_location_three",  query=True, text=True)
        # set attr
        cmds.textField("fk_crotch_shoulder_ctrl",  edit=True, text=one)
        cmds.textField("fk_Knee_elbow_ctrl",  edit=True, text=two)
        cmds.textField("fk_Ankle_wrist_ctrl",  edit=True, text=three)
    
    def fk_transfer_ik(self, *args):
        # get attr 
        one = cmds.textField("fk_crotch_shoulder_ctrl",  query=True, text=True)
        two = cmds.textField("fk_Knee_elbow_ctrl",  query=True, text=True)
        three = cmds.textField("fk_Ankle_wrist_ctrl",  query=True, text=True)
        # set attr
        cmds.textField("pickup_location_one",  edit=True, text=one)
        cmds.textField("pickup_location_two",  edit=True, text=two)
        cmds.textField("pickup_location_three",  edit=True, text=three)
    ##########################################################################################
    
    def Refresh(self, *args):
        # get time 
        currentTime = cmds.currentTime(query=True)
        time_max = cmds.playbackOptions(query=True, maxTime=True)
        time_min = cmds.playbackOptions(query=True, minTime=True)
        
        cmds.floatFieldGrp("set_time", edit=True, value=[currentTime, time_min, time_max, 0])
    
    #-------------------------#ik >>>> FK  的无缝切换-----------------------------------------
    def create_loc(self, *args):
        # create locator name 
        self.positioner_one = 'loc_ikfk_Seamless_switching_Polar_vector_001'
        self.replace_ik_controller = 'loc_replace_ik_controller_001'
        self.zero_replace_ik_controller = 'zero_replace_ik_controllerLoc_001'
        
        # create locator
        cmds.createNode('locator', name=self.positioner_one + 'Shape')
        cmds.createNode('locator', name=self.replace_ik_controller + 'Shape')
        cmds.createNode('transform', name=self.zero_replace_ik_controller)
        
        # parent 
        cmds.parent(self.replace_ik_controller, self.zero_replace_ik_controller)
        
        return self.zero_replace_ik_controller
    
    def if_fk_Seamless_switching(self, positioner_one, replace_ik_controller, zero_replace_ik_controller, 
                                    location_one, location_two, location_three, 
                                        Polar_vector, controllers, 
                                            time, current_time):
        """
            positioner_one(int) : locator loc
            replace_ik_controller(int) : locator loc
            zero_replace_ik_controller(int) : locator loc
            
            location_one(int) : fk crotch/shoulder controller name 
            location_two(int) : fk knee/elbow controller name 
            location_three(int) : fk ankle/wist controller name 
            
            Polar_vector(int) : ik polar vector controller name 
            controllers(int) : ik ankle/wrist controller name 
            
            time(float) : Default pose frame
            current_time(float) : Current pose frame
        """
        # get and set time
        cmds.setAttr('time1.outTime', time)
        
        # Obtain whether automatic k-frame is on
        autoKeyframe = cmds.autoKeyframe(query=True, state=True)
        if autoKeyframe == True:
            cmds.autoKeyframe(edit=True, state=False)
        
        # parent 
        cmds.parent(positioner_one, location_one)

        # set ik controller the zero 
        cmds.xform(Polar_vector, translation=[0, 0, 0])
        cmds.xform(controllers,  translation=[0, 0, 0], rotation=[0, 0, 0])
        
        # parentConstraint
        cmds.matchTransform(zero_replace_ik_controller, location_three, position=True, rotation=True)
        cmds.matchTransform(replace_ik_controller, location_three)
        cmds.matchTransform(positioner_one, Polar_vector)
        
        constraint_replace_ik_controller = cmds.parentConstraint(replace_ik_controller, controllers, 
                                                                                maintainOffset=True, weight=1)[0]
        cmds.setAttr(constraint_replace_ik_controller + '.interpType', 2)

        # set time
        cmds.setAttr('time1.outTime', current_time)
        
        # set ik controller
        cmds.matchTransform(replace_ik_controller, location_three)
        cmds.matchTransform(Polar_vector, positioner_one)
        
        cmds.delete(positioner_one)
        
        cmds.autoKeyframe(edit=True, state=autoKeyframe)
        
        return constraint_replace_ik_controller
    
    def if_fk_Seamless_switching_aim(self, positioner_one, replace_ik_controller, 
                                    zero_replace_ik_controller,
                                        location_one, location_two, location_three, 
                                            Polar_vector, controllers, 
                                                default_time, start_time, end_time):
        """
            positioner_one(int) : locator loc
            replace_ik_controller(int) : locator loc
            zero_replace_ik_controller(int) : locator loc
            
            location_one(int) : fk crotch/shoulder controller name 
            location_two(int) : fk knee/elbow controller name 
            location_three(int) : fk ankle/wist controller name 
            
            Polar_vector(int) : ik polar vector controller name 
            controllers(int) : ik ankle/wrist controller name 
        """
        # delet ik controller aim
        cmds.cutKey([Polar_vector, controllers], clear=True, time=(), 
                        hierarchy='none', controlPoints=False, shape=True)
        
        # get and set time
        cmds.setAttr('time1.outTime', default_time)
                
        # parent 
        cmds.parent(positioner_one, location_one)
                
        # set ik controller the zero 
        cmds.xform(Polar_vector, translation=[0, 0, 0])
        cmds.xform(controllers,  translation=[0, 0, 0], rotation=[0, 0, 0])
                
        # parentConstraint
        cmds.matchTransform(zero_replace_ik_controller, location_three, position=True, rotation=True)
        cmds.matchTransform(replace_ik_controller, location_three)
        cmds.matchTransform(positioner_one, Polar_vector)
                        
        # parentConstraint
        constraint_replace_ik_controller = cmds.parentConstraint(replace_ik_controller, controllers, 
                                                                    maintainOffset=True, weight=1)[0]
        cmds.setAttr(constraint_replace_ik_controller + '.interpType', 2)
        
        for time_i in range(int(start_time), int(end_time + 1)):
            # set Time frame
            cmds.currentTime(time_i)
            # set ik controller
            cmds.matchTransform(replace_ik_controller, location_three)
            cmds.matchTransform(Polar_vector, positioner_one)
            
            # Set keyframes
            cmds.setKeyframe([Polar_vector, replace_ik_controller], breakdown=False, hierarchy='none', 
                                        controlPoints=False, shape=True)
            
            # warning
            cmds.warning('Rate Of Progress: {}'.format(time_i))

        # controller bakeResults
        cmds.bakeResults(controllers, simulation=True, time=(int(start_time), int(end_time)), sampleBy=True, oversamplingRate=True, disableImplicitControl=True, 
                            preserveOutsideKeys=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, 
                                removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True ,
                                    controlPoints=False, shape=True)
                                    
        # warning
        cmds.warning('Handover Complete ! ! !')
        # Delete static frames
        cmds.delete([Polar_vector, controllers], staticChannels=True, unitlessAnimationCurves=False, hierarchy='none',
                        controlPoints=False, shape=True)

        # delete create none 
        cmds.delete(positioner_one, constraint_replace_ik_controller, zero_replace_ik_controller)
        
    def single_frame(self, *args):
        
        # Mirror on off 
        Mirror = cmds.checkBox('Mirror', query=True, value=True)
        
        # Animation on off
        Animation = cmds.checkBox('Animation', query=True, value=True)
        
        mirror_replace_one = cmds.textField('mirror_replace_one', query=True, text=True)
        mirror_replace_two = cmds.textField('mirror_replace_two', query=True, text=True)
        
        # fk ctrl name
        location_one = cmds.textField("pickup_location_one",  query=True,text=True)
        location_two = cmds.textField("pickup_location_two",  query=True,text=True)
        location_three = cmds.textField("pickup_location_three",  query=True,text=True)
        
        # ik ctrl name
        Polar_vector = cmds.textField("pickup_Polar_vector",  query=True, text=True)
        controllers = cmds.textField("pickup_controller",  query=True, text=True)
        
        # time 
        default_time = cmds.floatFieldGrp("set_time",query=True, value1=True)
        start_time = cmds.floatFieldGrp("set_time",query=True, value2=True)
        end_time = cmds.floatFieldGrp("set_time",query=True, value3=True)
        
        current_time = cmds.getAttr('time1.outTime')
        
        if Animation == True:
            if Mirror == True:
                
                Mirror_location_one = location_one.replace(mirror_replace_one, mirror_replace_two)
                Mirror_location_two = location_two.replace(mirror_replace_one, mirror_replace_two)
                Mirror_location_three = location_three.replace(mirror_replace_one, mirror_replace_two)
                            
                Mirror_Polar_vector = Polar_vector.replace(mirror_replace_one, mirror_replace_two)
                Mirror_controllers = controllers.replace(mirror_replace_one, mirror_replace_two)
                
                # one side
                self.create_loc()
                self.if_fk_Seamless_switching_aim(self.positioner_one, self.replace_ik_controller, 
                                                self.zero_replace_ik_controller,
                                                    location_one, location_two, location_three, 
                                                        Polar_vector, controllers, 
                                                            default_time, start_time, end_time)
                 # On the other side
                self.create_loc()
                self.if_fk_Seamless_switching_aim(self.positioner_one, self.replace_ik_controller, 
                                                self.zero_replace_ik_controller,
                                                    Mirror_location_one, Mirror_location_two, Mirror_location_three, 
                                                        Mirror_Polar_vector, Mirror_controllers, 
                                                            default_time, start_time, end_time)
            
            elif Mirror == False:
                self.create_loc()
                self.if_fk_Seamless_switching_aim(self.positioner_one, self.replace_ik_controller, 
                                                self.zero_replace_ik_controller,
                                                    location_one, location_two, location_three, 
                                                        Polar_vector, controllers, 
                                                            default_time, start_time, end_time)
                
        elif Animation == False:
            if Mirror == True:
                Mirror_location_one = location_one.replace(mirror_replace_one, mirror_replace_two)
                Mirror_location_two = location_two.replace(mirror_replace_one, mirror_replace_two)
                Mirror_location_three = location_three.replace(mirror_replace_one, mirror_replace_two)
                            
                Mirror_Polar_vector = Polar_vector.replace(mirror_replace_one, mirror_replace_two)
                Mirror_controllers = controllers.replace(mirror_replace_one, mirror_replace_two)
                            
                # one side
                del_loc = self.create_loc()
                del_point = self.if_fk_Seamless_switching(self.positioner_one, self.replace_ik_controller, 
                                                                    self.zero_replace_ik_controller,
                                                                        location_one, location_two, location_three, 
                                                                            Polar_vector, controllers, 
                                                                                default_time, current_time)
                # set key frame 
                cmds.setKeyframe([Polar_vector, controllers], breakdown=False, hierarchy='none', controlPoints=False, shape=True)
                cmds.delete(del_point, del_loc)
                # datele excessive key
                cmds.delete([controllers, Polar_vector], staticChannels=True, unitlessAnimationCurves=False, hierarchy='none',
                                controlPoints=False, shape=True)
                            
                # On the other side
                del_loc = self.create_loc()
                del_point = self.if_fk_Seamless_switching(self.positioner_one, self.replace_ik_controller, 
                                                                    self.zero_replace_ik_controller,
                                                                        Mirror_location_one, Mirror_location_two, Mirror_location_three, 
                                                                            Mirror_Polar_vector, Mirror_controllers, 
                                                                                default_time, current_time)
                # set key frame 
                cmds.setKeyframe([Mirror_controllers, Mirror_Polar_vector], breakdown=False, hierarchy='none', controlPoints=False, shape=True)
                cmds.delete(del_point, del_loc)
                # datele excessive key
                cmds.delete([Mirror_controllers, Mirror_Polar_vector], staticChannels=True, unitlessAnimationCurves=False, hierarchy='none',
                                controlPoints=False, shape=True)
            
            elif Mirror == False:
                del_loc = self.create_loc()
                del_point = self.if_fk_Seamless_switching(self.positioner_one, self.replace_ik_controller, 
                                                            self.zero_replace_ik_controller,
                                                                location_one, location_two, location_three, 
                                                                    Polar_vector, controllers, 
                                                                        default_time, current_time)
                # set key frame 
                cmds.setKeyframe([Polar_vector, controllers], breakdown=False, hierarchy='none', controlPoints=False, shape=True)
                cmds.delete(del_point, del_loc)
                # datele excessive key
                cmds.delete([controllers, Polar_vector], staticChannels=True, unitlessAnimationCurves=False, hierarchy='none',
                                controlPoints=False, shape=True)
    
    def ik_to_fk_create_location(self, ctrl_one, ctrl_two, ctrl_three):
        # create locator and group ==========#
        zero_one = 'zero_' + ctrl_one 
        zero_two = 'zero_' + ctrl_two 
        zero_three = 'zero_' + ctrl_three 

        loc_one = 'loc_' + ctrl_one 
        loc_two = 'loc_' + ctrl_two 
        loc_three = 'loc_' + ctrl_three 

        cmds.createNode('locator', name=loc_one + 'Shape')
        cmds.createNode('locator', name=loc_two + 'Shape')
        cmds.createNode('locator', name=loc_three + 'Shape')

        cmds.createNode('transform', name=zero_one)
        cmds.createNode('transform', name=zero_two)
        cmds.createNode('transform', name=zero_three)

        # locator parent transform
        cmds.parent(loc_one, zero_one)
        cmds.parent(loc_two, zero_two)
        cmds.parent(loc_three, zero_three)
        
        return [[zero_one, zero_two, zero_three], [loc_one, loc_two, loc_three]]
    
    def fk_to_ik_seamless_switching(self, ctrl_one, ctrl_two, ctrl_three, 
                                        jnt_one, jnt_two, jnt_three):
                                            
        create_location = self.ik_to_fk_create_location(ctrl_one, ctrl_two, ctrl_three)
        
        # set transform
        constraint_one = cmds.parentConstraint(jnt_one, create_location[1][0], weight=1)[0]
        constraint_two = cmds.parentConstraint(jnt_two, create_location[1][1], weight=1)[0]
        constraint_three = cmds.parentConstraint(jnt_three, create_location[1][2], weight=1)[0]

        # delete constraint
        cmds.delete(constraint_one)
        cmds.delete(constraint_two)
        cmds.delete(constraint_three)

        # set fk controller rotate
        cmds.matchTransform(ctrl_one, create_location[1][0], rotation=True)
        cmds.matchTransform(ctrl_two, create_location[1][1], rotation=True)
        cmds.matchTransform(ctrl_three, create_location[1][2], rotation=True)
        
        # delete location
        cmds.delete(create_location[0][0])
        cmds.delete(create_location[0][1])
        cmds.delete(create_location[0][2])
    
    def fk_to_ik_seamless_switching_animation(self, ctrl_one, ctrl_two, ctrl_three, 
                                        jnt_one, jnt_two, jnt_three, 
                                            start_time, end_time):
                                            
        create_location = self.ik_to_fk_create_location(ctrl_one, ctrl_two, ctrl_three)
        
        # set transform
        constraint_one = cmds.parentConstraint(jnt_one, create_location[1][0], weight=1)[0]
        constraint_two = cmds.parentConstraint(jnt_two, create_location[1][1], weight=1)[0]
        constraint_three = cmds.parentConstraint(jnt_three, create_location[1][2], weight=1)[0]
        
        
        for time_i in range(int(start_time), int(end_time) + 1):
            #cmds.setAttr('time1.outTime', time_i)
            cmds.currentTime(time_i)
            
            # set fk controller rotate
            cmds.matchTransform(ctrl_one, create_location[1][0], rotation=True)
            cmds.matchTransform(ctrl_two, create_location[1][1], rotation=True)
            cmds.matchTransform(ctrl_three, create_location[1][2], rotation=True)
            # Whether k frames

            cmds.setKeyframe([ctrl_one, ctrl_two, ctrl_three], 
                                breakdown=False, hierarchy='none', controlPoints=False, shape=False)
            
            # warning
            cmds.warning('Rate Of Progress: {}'.format(time_i))
        # warning
        cmds.warning('Handover Complete ! ! !')
        
        # Delete static frames
        cmds.delete([ctrl_one, ctrl_two, ctrl_three], 
                        staticChannels=True, unitlessAnimationCurves=False, 
                            hierarchy='none',controlPoints=False, shape=True)
        
        # delete constraint
        cmds.delete(constraint_one)
        cmds.delete(constraint_two)
        cmds.delete(constraint_three)
        
        # delete location
        cmds.delete(create_location[0][0])
        cmds.delete(create_location[0][1])
        cmds.delete(create_location[0][2])
    
    
    def run_ik_to_fk(self, *args):
        
        # Animation on off
        Animation = cmds.checkBox('Animation', query=True, value=True)
        
        # time
        start_time = cmds.floatFieldGrp("set_time",query=True, value2=True)
        end_time = cmds.floatFieldGrp("set_time",query=True, value3=True)
        
        # ctrl 
        ctrl_one = cmds.textField('fk_crotch_shoulder_ctrl', query=True, text=True)
        ctrl_two = cmds.textField('fk_Knee_elbow_ctrl', query=True, text=True)
        ctrl_three = cmds.textField('fk_Ankle_wrist_ctrl', query=True, text=True)

        # joint 
        jnt_one = cmds.textField('ik_crotch_shoulder_joint', query=True, text=True)
        jnt_two = cmds.textField('ik_Knee_elbow_joint', query=True, text=True)
        jnt_three = cmds.textField('ik_Ankle_wrist_joint', query=True, text=True)
        
        # Mirror
        Mirror = cmds.checkBox('Mirror', query=True, value=True)
        
        mirror_replace_one = cmds.textField('mirror_replace_one', query=True, text=True)
        mirror_replace_two = cmds.textField('mirror_replace_two', query=True, text=True)
        
        #========================================================================#
        mirror_ctrl_one = ctrl_one.replace(mirror_replace_one, mirror_replace_two)
        mirror_ctrl_two = ctrl_two.replace(mirror_replace_one, mirror_replace_two)
        mirror_ctrl_three = ctrl_three.replace(mirror_replace_one, mirror_replace_two)
        
        mirror_jnt_one = jnt_one.replace(mirror_replace_one, mirror_replace_two)
        mirror_jnt_two = jnt_two.replace(mirror_replace_one, mirror_replace_two)
        mirror_jnt_three = jnt_three.replace(mirror_replace_one, mirror_replace_two)
        #========================================================================#
        if Animation == True:
            if Mirror == True:
                self.fk_to_ik_seamless_switching_animation(ctrl_one, ctrl_two, ctrl_three, 
                                                    jnt_one, jnt_two, jnt_three, 
                                                        start_time, end_time)
                                                    
                self.fk_to_ik_seamless_switching_animation(mirror_ctrl_one, mirror_ctrl_two, mirror_ctrl_three, 
                                                    mirror_jnt_one, mirror_jnt_two, mirror_jnt_three, 
                                                        start_time, end_time)
            elif Mirror == False:
                self.fk_to_ik_seamless_switching_animation(ctrl_one, ctrl_two, ctrl_three, 
                                                    jnt_one, jnt_two, jnt_three, 
                                                        start_time, end_time)
        
        if Animation == False:
            if Mirror == True:
                self.fk_to_ik_seamless_switching(ctrl_one, ctrl_two, ctrl_three, 
                                                    jnt_one, jnt_two, jnt_three)
                                                    
                self.fk_to_ik_seamless_switching(mirror_ctrl_one, mirror_ctrl_two, mirror_ctrl_three, 
                                                    mirror_jnt_one, mirror_jnt_two, mirror_jnt_three)
            elif Mirror == False:
                self.fk_to_ik_seamless_switching(ctrl_one, ctrl_two, ctrl_three, 
                                                    jnt_one, jnt_two, jnt_three)
        
    
run = FK_TO_IK()



