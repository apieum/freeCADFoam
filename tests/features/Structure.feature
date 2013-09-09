Feature: Create a case
    In Order to make a simulation
    As scientist
    I need to create a case

    Scenario: Add a case object to the scene
        Given FreeCAD gui is initialized
        And OpenFoam workbench is loaded
        When I create a Case
        Then document contains a case object
        And case object contains a case view provider
