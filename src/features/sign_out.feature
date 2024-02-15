
@android
Feature: Sign Out

  @skip
  Scenario: Log Out
  Given user is at Account Page
  When user taps in sign out
  Then app close session and shows phone number page
