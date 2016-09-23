== == == == == == == == == == == == == == == == =
PyCharm
2.6
.2
Setup
for Maya 2013
    == == == == == == == == == == == == == == == == =

    Prerequisites:
    --------------

    *Your
    OS is windows
    7(Assumed
    to
    be
    x64)
    *Download and install
    PyCharm:  http: // www.jetbrains.com / pycharm / download /
    *AutoDesk
    Maya is installed

    Instructions:
    -------------

    1.
    Create
    a
    symbolic
    link
    to
    mayapy.exe

    *Open
    a
    command
    prompt
    with admin rights:
        Start > All
        Programs > Accessories > right
        click
        on
        Command
        Prompt > Run as Administrator > Click[Yes]
        at
        UAC
        Dialog
        popup

    *Navigate
    to
    Maya
    's bin directory:
    cd
    "c:\Program Files\Autodesk\Maya2013\bin"

    *Make
    a
    symbolic
    link
    from mayapy.exe to

    python.exe(This
    essentially
    creates
    a
    renamed
    exe
    shortcut)
    You
    should
    see, "sybmolic link created for python.exe <<==>> mayapy.exe"
    if successful:
        mklink
        python.exe
        mayapy.exe

    2.
    Configure
    PyCharm
    Maya
    Interpreter

    *Open
    PyCharm

    *Open
    the
    settings
    window
    File -> Settings...

    *Add
    our
    python.exe
    symlink as a
    python
    interpreter:
    *Navigate
    to
    Settings > Template
    Project
    Settings > Project
    Interpreter > Python
    Interpreter
    *click
    the[Add]
    button(plus
    icon) on
    the
    top
    far
    right
    *select
    "Local..."
    from the Select

    Interpreter
    Path
    dialog
    *select
    our
    "python.exe"
    symlink
    found
    at
    "C:\Program Files\Autodesk\Maya2013\bin\python.exe"
    from the selection

    dialog
    *hit
    the[OK]
    button and wait
    while PyCharm updates skeletons

    Leave
    this
    window
    up, don
    't close it!

    *Configure
    the
    Paths
    for our newly added interpreter:
        *With
        our
        newly
        added
        interpreter
        selected in the
        top
        pane, click
        on
        the
        _Paths_
        tab in the
        bottom
        pane
        of
        the
        Python
        Interpreters
        window
        *Add
        path
        to
        AutoDesk
        provided
        stub
        files(This
        seemed
        to
        fix
        completion
        issues
        I
        was
        having):
        *Click
        the[Add]
        button(plus
        icon) on
        the
        top
        right
        of
        the
        _Paths_
        pane
        *Navigate
        to and select
        "C:\Program Files\Autodesk\Maya2013\devkit\other\pymel\extras\completion\py"
        then
        click[OK]
        button
    *Remove
    Maya
    's site-packages entry (only if you added the stubs outlined above)
    *Select
    the
    entry
    for "C:\Program Files\Autodesk\Maya2013\Python\Lib\site-packages"
        *Click
        the[Remove]
        button(minus
        icon)
        *Add
        path
        Jetbrains
        Helpers(
        for remote debugging)
        *Click
        the[Add]
        button(plus
        icon) on
        the
        top
        right
        of
        the
        _Paths_
        pane
        *Navigate
        to and select
        "C:\Program Files (x86)\JetBrains\PyCharm 2.6.2\helpers"
        then
        click[OK]
        button
        *OPTIONAL: Add
        any
        other
        sys
        paths
        you
        wish
        to
        incorporate
        here
        using
        same
        add
        steps as above

        *Close
        PyCharm and Reopen
        it
        for paths to take affect

        3.
        Configure
        PyCharm
        Maya
        remote
        debugger

        *From
        the
        Run
        menu
        of
        PyCharm
        choose
        "Edit Configurations..."

        *Configure
        the
        Unnamed
        debugger
        which
        appears as follows:

        *Change
        Name
        field
        from

        "Unnamed"
        to
        "Maya 2013"(This
        value
        names
        the
        debugging
        process, feel
        free
        to
        choose
        any
        name)
        *Change
        port
        from

        "0"
        to
        "7720"(This
        number
        determines
        the
        port
        which
        traffics
        communication, feel
        free
        to
        use
        another
        port)
        *Check[x]
        Check
        no
        other
        instances
        are
        running
        *OPTIONAL:  Uncheck[]
        Redirect
        output
        to
        console(to
        prevent
        output
        redirection
        from Maya)
        *OPTIONAL:  Uncheck[]
        Suspend
        after
        connect(to
        only
        pause
        at
        a
        breakpoint)

        Note: settings in this
        window
        affect
        the
        code
        necessary
        to
        trip
        the
        remote
        debugger, displayed in sections
        2 and 3.
        Be
        sure
        to
        write
        it
        down( or re - open
        this
        configuration
        window
        later
        to
        retrieve
        it
        later)

        4.
        Remote
        Debugging
        from Maya

        *In
        PyCharm:
        *Select
        the
        "Maya 2013"
        Remote
        Debug
        profile
        from the Run / Debug
        dropdown
        just
        below
        the
        main
        menubar
        *Click
        the
        green
        debug
        icon
        next
        to
        the
        dropdown
        to
        start
        PyCharm
        's server
        *You
        will
        see
        a
        debug
        console
        appear
        below
        the
        main
        code
        window
        indicating
        the
        server is awaiting
        a
        connection
        *Load
        the
        code
        you
        wish
        to
        step
        through, and ensure
        there
        's a breakpoint set somewhere within the code
        *Paste
        the
        server
        configuration
        code
        from step

        3
        's note into your code somewhere before your breakpoint and save the file.

        *In
        Maya:
        *Ensure
        that
        "C:\Program Files (x86)\JetBrains\PyCharm 2.6.2\helpers" is part
        of
        your
        sys.path(there
        are
        numerous
        ways
        to
        do
        this)

        pydev_path = r'C:\Program Files (x86)\JetBrains\PyCharm 2.6.2\helpers'
        if not pydev_path in sys.path:
            sys.path.append(pydev_path)

        *Import
        your and execute
        the
        code
        to
        remote
        debug.If
        all
        goes
        well, PyCharm
        should
        hold
        the
        code
        at
        your
        breakpoint, allowing
        you
        to
        navigate
        the
        code
        using
        the
        bottom
        Debugger
        pane