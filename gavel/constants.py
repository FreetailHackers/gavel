ANNOTATOR_ID = 'annotator_id'
TELEMETRY_URL = ''

# Setting
# keys
SETTING_CLOSED = 'closed' # boolean
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
**Please read this important message carefully before continuing.**

Gavel is a fully automated expo judging system that both tells you where to go
and collects your votes.

You'll start off by looking at a single submission. If this submission is not
at their location, press the 'Skip' button. For every submission after that,
you'll decide whether it's better or worse than the one you looked at
**immediately before**. Repeat this process until you've seen all submissions!

**Please don't skip unless it's absolutely necessary, and think hard
before you vote. Once you make a decision, you can't take it back.**
'''.strip()

DEFAULT_BEGIN_MESSAGE = '''
Please press "Done" once you have looked over this project. Press "Skip" if you cannot find this project at the assigned table.

Your **first** vote will be recorded on the **next** team, since the system records votes based on how good a team is to the previous team you've seen.
'''.strip()

DEFAULT_VOTE_MESSAGE = '''
Press "Previous" if you think the previous project is better than the current project, and press "Current" if you like the current project is better than the previous one.

Press "Skip" if you cannot find the current project at the assigned table.
'''.strip()

DEFAULT_EMAIL_SUBJECT = 'Welcome to HackTX Judging!'

DEFAULT_EMAIL_BODY = '''
Hi {name},

Welcome to Gavel, the online expo judging system that HackTX is using. This email contains your
magic link to the judging system.

DO NOT SHARE this email with others, as it contains your personal magic link.

To access the system, visit {link}.

Once you're in, please take the time to read the welcome message and
instructions before continuing.
'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The judging system is currently closed. Reload the page to try again once the system has been opened.
'''.strip()

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Please contact an organizer to remedy the situation.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open your magic link to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
Wait for a little bit and reload the page to try again.

If you've looked at all the projects already, then you're done.
'''.strip()
