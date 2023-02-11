#include <X11/Xlib.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#include <unistd.h>

#include <X11/Xlib.h>
#include <X11/Xutil.h>

void mouseClick(int button)
{
    Display *display = XOpenDisplay(NULL);

    XEvent event;

    if (!display)
    {
        fprintf(stderr, "Cannot initialize the display\n");
        exit(EXIT_FAILURE);
    }

    memset(&event, 0x00, sizeof(event));

    event.type = ButtonPress;
    event.xbutton.button = button;
    // indicates whether the event window is on the same screen as the root window
    event.xbutton.same_screen = True;

    // returns the root window the pointer is logically on and the pointer coordinates
    // relative to the root window's origin
    XQueryPointer(display, RootWindow(display, DefaultScreen(display)), &event.xbutton.root,
        &event.xbutton.window, &event.xbutton.x_root, &event.xbutton.y_root, &event.xbutton.x,
        &event.xbutton.y, &event.xbutton.state);

    event.xbutton.subwindow = event.xbutton.window;
    // while the pointer is in the subwindow -> get it from there
    while(event.xbutton.subwindow)
    {
        // window used by the X server to report the event
        event.xbutton.window = event.xbutton.subwindow;
        XQueryPointer(display, event.xbutton.window, &event.xbutton.root, &event.xbutton.subwindow,
            &event.xbutton.x_root, &event.xbutton.y_root, &event.xbutton.x, &event.xbutton.y,
            &event.xbutton.state);
    }

    if (XSendEvent(display, PointerWindow, True, 0xfff, &event) == 0)
    {
        fprintf(stderr, "Error\n");
    }

    XFlush(display);
    usleep(50000);

    event.type = ButtonRelease;
    event.xbutton.state = 0x100; // Button1Mask

    // 2d param - Specifies the window the event is to be sent to, or PointerWindow, or InputFocus.
    // 0xfff - event mask
    if (XSendEvent(display, PointerWindow, True, 0xfff, &event) == 0)
    {
        fprintf(stderr, "Error\n");
    }

    XFlush(display);
    usleep(250000); // avarage interval between double click

    event.type = ButtonPress;
    event.xbutton.state = 0x100; // Button1Mask

    // 2d param - Specifies the window the event is to be sent to, or PointerWindow, or InputFocus.
    // 0xfff - event mask
    if (XSendEvent(display, PointerWindow, True, 0xfff, &event) == 0)
    {
        fprintf(stderr, "Error\n");
    }

    XFlush(display);
    usleep(50000);

    event.type = ButtonRelease;
    event.xbutton.state = 0x100; // Button1Mask

    if (XSendEvent(display, PointerWindow, True, 0xfff, &event) == 0)
    {
        fprintf(stderr, "Error\n");
    }

    XFlush(display);
    XCloseDisplay(display);
}
int main(int argc,char * argv[]) {

    int x , y;
    x=atoi(argv[1]);
    y=atoi(argv[2]);

    // open a connection to the X server that controls a display
    Display *display = XOpenDisplay(0);

    // returns the root window for the default screen
    Window root = DefaultRootWindow(display);

    // generates events just as if the user had instantaneously
    // moved the pointer from one position to another
    // 3d parameter is dest_w, if it is not None, XWarpPointer()
    // moves the pointer to the offsets (dest_x, dest_y) relative to the origin of dest_w
    XWarpPointer(display, None, root, 0, 0, 0, 0, x, y);
    XFlush(display);

    usleep(1000000);

    mouseClick(Button1);

    XFlush(display);
    XCloseDisplay(display);
    return 0;
}

