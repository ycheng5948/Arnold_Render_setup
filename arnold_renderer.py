import maya.cmds as cmds
from mtoa.cmds.arnoldRender import arnoldRender
# render settings
# adjust based on each render session's parameters
# below is just an example
# common
cmds.setAttr("defaultRenderGlobals.imageFilePrefix", "", type="string")
cmds.setAttr("defaultRenderGlobals.extensionPadding", 2)
cmds.setAttr("defaultRenderGlobals.byFrameStep", 1)

# system
cmds.setAttr("defaultArnoldRenderOptions.AASamples", 4)
cmds.setAttr("defaultArnoldRenderOptions.GIDiffuseSamples", 4)
cmds.setAttr("defaultArnoldRenderOptions.GISpecularSamples", 4)
cmds.setAttr("defaultArnoldRenderOptions.GITransmissionSamples", 0)
cmds.setAttr("defaultArnoldRenderOptions.GISssSamples", 0)
cmds.setAttr("defaultArnoldRenderOptions.GITotalDepth", 10)
cmds.setAttr("defaultArnoldRenderOptions.GIDiffuseDepth", 5)
cmds.setAttr("defaultArnoldRenderOptions.GISpecularDepth", 5)
cmds.setAttr("defaultArnoldRenderOptions.GITransmissionDepth", 0)
cmds.setAttr("defaultArnoldRenderOptions.GIVolumeDepth", 0)
cmds.setAttr("defaultArnoldRenderOptions.autoTransparencyDepth", 0)

# AOVs
cmds.setAttr("defaultArnoldRenderOptions.denoiseBeauty", 1)
cmds.setAttr("defaultArnoldRenderOptions.outputVarianceAOVs", 1)

def render_seq(camera_name, start_frame, end_frame, filename):
    """
    Renders a sequence of frames for a specific camera.

    Args:
        camera_name: The name of the camera to render.
        start_frame: The starting frame number.
        end_frame: The ending frame number.
        filename: The filename to override the default setting.
    """
  
    # layer
    cmds.editRenderLayerGlobals( currentRenderLayer='masterLayer')

    cmds.setAttr("defaultArnoldDriver.ai_translator", "exr", type="string")
    if filename:
        cmds.setAttr("defaultArnoldDriver.pre", filename, type="string")
    
    end_frame+=1

    for x in range(start_frame, end_frame):
        cmds.currentTime(x)
        arnoldRender(1280, 720, True, True, camera_name, ' -layer masterLayer -o {0}'.format(output_path))
    print("Render Completed!")
