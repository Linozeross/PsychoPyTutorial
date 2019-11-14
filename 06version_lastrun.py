#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Thu Nov 14 14:42:22 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = '06version'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'practice': True}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/lino/Documents/UniKiel/FP/06version_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='Drücken Sie die Leertaste wenn das angezeigte Kreuz rot ist.\nDrücken Sie keine Taste falls das angezeigte Kreuz NICHT rot ist.\n\nDrücken Sie die Leertaste zum starten!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.GratingStim(
    win=win, name='fixation',
    tex='sin', mask='gauss',
    ori=0, pos=(0, 0), size=(0.1, 0.1), sf=0, phase=0.0,
    color=[-1,-1,-1], colorSpace='rgb', opacity=1.0,blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)
go_item = visual.ShapeStim(
    win=win, name='go_item', vertices='cross',
    size=(0.3, 0.3),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
#Dies ist ein Kommentar
#Wir müssen am Anfang des Experiments das random Modul (von python)
#importieren um Zugriff auf einen Zufallsgenerator zu haben
import random

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
#Definiere variable msg (zeigt später unseren Feedback Text an)
msg = 'Default Text'

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.GratingStim(
    win=win, name='fixation',
    tex='sin', mask='gauss',
    ori=0, pos=(0, 0), size=(0.1, 0.1), sf=0, phase=0.0,
    color=[-1,-1,-1], colorSpace='rgb', opacity=1.0,blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)
go_item = visual.ShapeStim(
    win=win, name='go_item', vertices='cross',
    size=(0.3, 0.3),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
#Dies ist ein Kommentar
#Wir müssen am Anfang des Experiments das random Modul (von python)
#importieren um Zugriff auf einen Zufallsgenerator zu haben
import random

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instr_resp = keyboard.Keyboard()
# keep track of which components have finished
instructionComponents = [instr, instr_resp]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if t >= 0.0 and instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr.tStart = t  # not accounting for scr refresh
        instr.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        instr.setAutoDraw(True)
    
    # *instr_resp* updates
    if t >= 1.0 and instr_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_resp.tStart = t  # not accounting for scr refresh
        instr_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
        instr_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
        instr_resp.clearEvents(eventType='keyboard')
    if instr_resp.status == STARTED:
        theseKeys = instr_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            instr_resp.keys = theseKeys.name  # just the last key pressed
            instr_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr.started', instr.tStartRefresh)
thisExp.addData('instr.stopped', instr.tStopRefresh)
# check responses
if instr_resp.keys in ['', [], None]:  # No response was made
    instr_resp.keys = None
thisExp.addData('instr_resp.keys',instr_resp.keys)
if instr_resp.keys != None:  # we had a response
    thisExp.addData('instr_resp.rt', instr_resp.rt)
thisExp.addData('instr_resp.started', instr_resp.tStartRefresh)
thisExp.addData('instr_resp.stopped', instr_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('03loop.xlsx'),
    seed=None, name='practiceLoop')
thisExp.addLoop(practiceLoop)  # add the loop to the experiment
thisPracticeLoop = practiceLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in practiceLoop:
    #neu, manuell hinzugefügt:
    if (expInfo['practice'] == False): 
        break
        
    currentLoop = practiceLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    fixation.setOpacity(1)
    go_item.setOpacity(1)
    go_item.setFillColor(go_color)
    key_resp = keyboard.Keyboard()
    #random.random() gibt einen zufälligen Wert zwischen 0.0 und 1.0 aus
    #50% der Fälle entspricht also >0.5
    if (random.random() > 0.5): #entweder mache dies:
        #setze stim_pos Variable auf (-2,0)
        stim_pos = (-0.5,0)
    else: #oder mache das:
        stim_pos = (0.5,0)
    
    # keep track of which components have finished
    trialComponents = [fixation, go_item, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # not accounting for scr refresh
            fixation.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        frameRemains = 0.0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
            fixation.setAutoDraw(False)
        
        # *go_item* updates
        if t >= 2.5 and go_item.status == NOT_STARTED:
            # keep track of start time/frame for later
            go_item.tStart = t  # not accounting for scr refresh
            go_item.frameNStart = frameN  # exact frame index
            win.timeOnFlip(go_item, 'tStartRefresh')  # time at next scr refresh
            go_item.setAutoDraw(True)
        frameRemains = 2.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if go_item.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            go_item.tStop = t  # not accounting for scr refresh
            go_item.frameNStop = frameN  # exact frame index
            win.timeOnFlip(go_item, 'tStopRefresh')  # time at next scr refresh
            go_item.setAutoDraw(False)
        if go_item.status == STARTED:  # only update if drawing
            go_item.setPos(stim_pos, log=False)
        
        # *key_resp* updates
        if t >= 2.5 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # not accounting for scr refresh
            key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            key_resp.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
            key_resp.status = FINISHED
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space', None], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceLoop.addData('fixation.started', fixation.tStartRefresh)
    practiceLoop.addData('fixation.stopped', fixation.tStopRefresh)
    practiceLoop.addData('go_item.started', go_item.tStartRefresh)
    practiceLoop.addData('go_item.stopped', go_item.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practiceLoop (TrialHandler)
    practiceLoop.addData('key_resp.keys',key_resp.keys)
    practiceLoop.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        practiceLoop.addData('key_resp.rt', key_resp.rt)
    practiceLoop.addData('key_resp.started', key_resp.tStartRefresh)
    practiceLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.addData('stimulusPosition',stim_pos)
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    feedbackComponents = [text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # not accounting for scr refresh
            text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
        if text.status == STARTED:  # only update if drawing
            text.setText(msg, log=False)
        if (key_resp.corr == 1):
            msg = "Richtig!"
        else:
            msg = "Leider falsch."
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceLoop.addData('text.started', text.tStartRefresh)
    practiceLoop.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practiceLoop'


# set up handler to look after randomisation of conditions etc
fuenfMal = data.TrialHandler(nReps=2, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('03loop.xlsx'),
    seed=None, name='fuenfMal')
thisExp.addLoop(fuenfMal)  # add the loop to the experiment
thisFuenfMal = fuenfMal.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFuenfMal.rgb)
if thisFuenfMal != None:
    for paramName in thisFuenfMal:
        exec('{} = thisFuenfMal[paramName]'.format(paramName))

for thisFuenfMal in fuenfMal:
    currentLoop = fuenfMal
    # abbreviate parameter names if possible (e.g. rgb = thisFuenfMal.rgb)
    if thisFuenfMal != None:
        for paramName in thisFuenfMal:
            exec('{} = thisFuenfMal[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    fixation.setOpacity(1)
    go_item.setOpacity(1)
    go_item.setFillColor(go_color)
    key_resp = keyboard.Keyboard()
    #random.random() gibt einen zufälligen Wert zwischen 0.0 und 1.0 aus
    #50% der Fälle entspricht also >0.5
    if (random.random() > 0.5): #entweder mache dies:
        #setze stim_pos Variable auf (-2,0)
        stim_pos = (-0.5,0)
    else: #oder mache das:
        stim_pos = (0.5,0)
    
    # keep track of which components have finished
    trialComponents = [fixation, go_item, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # not accounting for scr refresh
            fixation.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        frameRemains = 0.0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
            fixation.setAutoDraw(False)
        
        # *go_item* updates
        if t >= 2.5 and go_item.status == NOT_STARTED:
            # keep track of start time/frame for later
            go_item.tStart = t  # not accounting for scr refresh
            go_item.frameNStart = frameN  # exact frame index
            win.timeOnFlip(go_item, 'tStartRefresh')  # time at next scr refresh
            go_item.setAutoDraw(True)
        frameRemains = 2.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if go_item.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            go_item.tStop = t  # not accounting for scr refresh
            go_item.frameNStop = frameN  # exact frame index
            win.timeOnFlip(go_item, 'tStopRefresh')  # time at next scr refresh
            go_item.setAutoDraw(False)
        if go_item.status == STARTED:  # only update if drawing
            go_item.setPos(stim_pos, log=False)
        
        # *key_resp* updates
        if t >= 2.5 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # not accounting for scr refresh
            key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            key_resp.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
            key_resp.status = FINISHED
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space', None], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fuenfMal.addData('fixation.started', fixation.tStartRefresh)
    fuenfMal.addData('fixation.stopped', fixation.tStopRefresh)
    fuenfMal.addData('go_item.started', go_item.tStartRefresh)
    fuenfMal.addData('go_item.stopped', go_item.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for fuenfMal (TrialHandler)
    fuenfMal.addData('key_resp.keys',key_resp.keys)
    fuenfMal.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        fuenfMal.addData('key_resp.rt', key_resp.rt)
    fuenfMal.addData('key_resp.started', key_resp.tStartRefresh)
    fuenfMal.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.addData('stimulusPosition',stim_pos)
    thisExp.nextEntry()
    
# completed 2 repeats of 'fuenfMal'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
