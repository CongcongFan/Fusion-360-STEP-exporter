import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Get the active design.
        design = app.activeProduct
        if not design:
            ui.messageBox('No active Fusion design', 'Export Error')
            return

        # Ask user for the directory to save the STEP files.
        dlg = ui.createFolderDialog()
        dlg.title = 'Select Folder to Save STEP Files'
        if dlg.showDialog() != adsk.core.DialogResults.DialogOK:
            return
        
        folder = dlg.folder

        # Loop through all components and export each one as a STEP file.
        for comp in design.rootComponent.allOccurrences:
            filename = folder + '/' + comp.component.name + '.step'
            stepExportOptions = design.exportManager.createSTEPExportOptions(filename, comp.component)
            design.exportManager.execute(stepExportOptions)

        ui.messageBox('Export completed successfully!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))