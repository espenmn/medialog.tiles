# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.tiles -t test_tiles.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.tiles.testing.MEDIALOG_TILES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_tiles.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Tiles
  Given a logged-in site administrator
    and an add tiles form
   When I type 'My Tiles' into the title field
    and I submit the form
   Then a tiles with the title 'My Tiles' has been created

Scenario: As a site administrator I can view a Tiles
  Given a logged-in site administrator
    and a tiles 'My Tiles'
   When I go to the tiles view
   Then I can see the tiles title 'My Tiles'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add tiles form
  Go To  ${PLONE_URL}/++add++Tiles

a tiles 'My Tiles'
  Create content  type=Tiles  id=my-tiles  title=My Tiles


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the tiles view
  Go To  ${PLONE_URL}/my-tiles
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a tiles with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the tiles title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
