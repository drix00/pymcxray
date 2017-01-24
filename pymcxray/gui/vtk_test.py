import vtk

if __name__ == '__main__':
    # create a Sphere
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(0.0, 1.0, 1.0)
    sphereSource.SetRadius(0.5)
    sphereSource.SetPhiResolution(100)
    sphereSource.SetThetaResolution(100)

    # create a mapper
    sphereMapper = vtk.vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    # create an actor
    sphereActor = vtk.vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.GetProperty().SetColor(1, 0, 0)
    sphereActor.GetProperty().SetOpacity(0.2)
    sphereActor.GetProperty().SetEdgeVisibility(True)

    # create cube
    cube = vtk.vtkCubeSource()
    cube.SetCenter(0.0, -1.0, -1.0)
    cube.SetBounds(0.0, 1.0, 0.0, 2.0, 0.0, 3.0)

    # mapper
    cubeMapper = vtk.vtkPolyDataMapper()
    #cubeMapper.SetInputData(cube.GetOutput())
    cubeMapper.SetInputConnection(cube.GetOutputPort())

    # actor
    cubeActor = vtk.vtkActor()
    cubeActor.SetMapper(cubeMapper)
    cubeActor.GetProperty().SetColor(0, 1, 0)
    cubeActor.GetProperty().SetOpacity(0.2)
    cubeActor.GetProperty().SetEdgeVisibility(True)

    # create source
    cylinder_source = vtk.vtkCylinderSource()
    cylinder_source.SetCenter(0, 0, 0)
    cylinder_source.SetRadius(5.0)
    cylinder_source.SetHeight(7.0)
    cylinder_source.SetResolution(100)

    # mapper
    cylinder_mapper = vtk.vtkPolyDataMapper()
    cylinder_mapper.SetInputConnection(cylinder_source.GetOutputPort())

    # actor
    cylinder_actor = vtk.vtkActor()
    cylinder_actor.SetMapper(cylinder_mapper)
    cylinder_actor.GetProperty().SetColor(0, 0, 1)
    cylinder_actor.GetProperty().SetOpacity(0.2)
    cylinder_actor.GetProperty().SetEdgeVisibility(True)

    # create a rendering window and renderer
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # create a renderwindowinteractor
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renderWindow)

    # assign actor to the renderer
    renderer.AddActor(cubeActor)
    renderer.AddActor(sphereActor)
    renderer.AddActor(cylinder_actor)
    renderer.SetBackground(0.1, .2, .3)

    transform = vtk.vtkTransform()
    transform.Translate(8.0, 0.0, 0.0)
    transform.Scale(4.0, 4.0, 4.0)

    axes = vtk.vtkAxesActor()
    #  The axes are positioned with a user transform
    axes.SetUserTransform(transform)

    # properties of the axes labels can be set as follows
    # this sets the x axis label to red
    # axes->GetXAxisCaptionActor2D()->GetCaptionTextProperty()->SetColor(1,0,0);

    # the actual text of the axis label can be changed:
    # axes->SetXAxisLabelText("test");

    renderer.AddActor(axes)

    renderer.ResetCamera()
    renderWindow.Render()

    # enable user interface interactor
    iren.Initialize()
    renderWindow.Render()
    iren.Start()