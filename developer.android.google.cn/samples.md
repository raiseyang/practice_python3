AppShortcuts
This sample demonstrates how to use the Launcher Shortcuts API introduced in Android 7.1 (API 25). This API allows an application to define a set of Intents which are displayed as when a user long-presses on the app's launcher icon. Examples are given for registering both links both statically in XML, as well as dynamically at runtime.
AutofillFramework
This sample demonstrates the use of the Autofill Framework. It includes implementations of client Activities that want to be autofilled, and a Service that can provide autofill data to client Activities. For simplicity, this sample's service uses mock data to autofill what it thinks are username and password text fields.
AutofillFramework (Kotlin)
This sample demonstrates the use of the Autofill Framework. It includes implementations of client Activities that want to be autofilled, and a Service that can provide autofill data to client Activities. For simplicity, this sample's service uses mock data to autofill what it thinks are username and password text fields.
DownloadableFonts
This sample demonstrates how to use the Downloadable Fonts feature introduced in Android O. Downloadable Fonts is a feature that allows apps to request a certain font from a provider instead of bundling it or downloading it themselves. This means, there is no need to bundle the font as an asset.
DownloadableFonts (Kotlin)
This sample demonstrates how to use the Downloadable Fonts feature introduced in Android O. Downloadable Fonts is a feature that allows apps to request a certain font from a provider instead of bundling it or downloading it themselves. This means, there is no need to bundle the font as an asset.
EmojiCompat
This sample demonstrates usage of EmojiCompat support library. You can use this library to prevent your app from showing missing emoji characters in the form of tofu (¡õ). You can use either bundled or downloadable emoji fonts. This sample shows both usages.
EmojiCompat (Kotlin)
This sample demonstrates usage of EmojiCompat support library. You can use this library to prevent your app from showing missing emoji characters in the form of tofu (¡õ). You can use either bundled or downloadable emoji fonts. This sample shows both usages.
JobScheduler
Demonstration of the JobScheduler API, which provides an interface for scheduling background tasks when certain tasks apply.
NotificationChannels
Demonstration of using channels to categorize notifications by topic. This feature was added in Android O, and allows users to have fine-grained control over their notification preferences.
NotificationChannels (Kotlin)
Demonstration of using channels to categorize notifications by topic. This feature was added in Android O, and allows users to have fine-grained control over their notification preferences.
PictureInPicture
This sample demonstrates basic usage of Picture-in-Picture mode for handheld devices. The sample plays a video. The video keeps on playing when the app is turned in to Picture-in-Picture mode. On Picture-in-Picture screen, the app shows an action item to pause or resume the video.
PictureInPicture (Kotlin)
This sample demonstrates basic usage of Picture-in-Picture mode for handheld devices. The sample plays a video. The video keeps on playing when the app is turned in to Picture-in-Picture mode. On Picture-in-Picture screen, the app shows an action item to pause or resume the video.
RuntimePermissions
This sample shows runtime permissions available in Android M and above. It shows how to check and request permissions at runtime, handle backwards compatibility using the support library and how to declare optional permissions for M-devices only.
AAudios
These samples demonstrate how to use AAudio API: 1. hello-aaudio sample: creates an output stream 1. echo sample: creates output and input streams, then play via loopback
android-ndk thread addresses some of the possible questions surrounding the new API.
AsymmetricFingerprintDialog
A sample that demonstrates to use registered fingerprints to authenticate the user in your app
CommitContentSampleApp
This sample demonstrates how to write an application which accepts rich content (such as images) sent from a keyboard using the Commit Content API.
CommitContentSampleIME
This sample demonstrates how to write an keyboard which sends rich content (such as images) to text fields using the Commit Content API.
DirectBoot
Sample demonstrating how to store data in a device protected storage which is always available while the device is booted both before and after any user credentials(PIN/Pattern/Password) are entered.
FingerprintDialog
A sample that demonstrates to use registered fingerprints to authenticate the user in your app
Firebase Quickstarts for Android
A collection of quickstart samples demonstrating the Firebase APIs on Android. For more information, see https://firebase.google.com.
MessagingService
This sample shows a simple service that sends notifications using NotificationCompat. It also extends the notification with Remote Input to allow Android N devices to reply via text directly from the notification without having to open an App. The same Remote Input object also allows Android Auto users to respond by voice when the notification is presented there. Note: Each unread conversation from a user is sent as a distinct notification.
RecipeAssistant
This phone application uses the enhanced notifications API to display recipe instructions using paged notifications. After starting the application on your phone, you can browse from a short list of recipes and select one to view. Each recipe is broken down into a number of steps; when ready, you can click on the START action in the action bar to send the steps to the wearable. On the wearable device, the steps are displayed as a multi-page notification, with one page for each step in the recipe.
WatchFace
A simple sample that demonstrates watch faces and complications for Wear 2.0.
WearDrawers
A simple sample that demonstrates Navigation and Action Drawers, part of Material Design for Wear.
WearHighBandwidthNetworking
Sample demonstrates how to determine if a high-bandwidth network is available for use cases that require a minimum network bandwidth, such as streaming media or downloading large files. In addition, the sample demonstrates best practices for asking a user to add a new Wi-Fi network for high-bandwidth network operations if the bandwidth of currently available networks is inadequate.
ActionBarCompat-Basic
This sample shows you how to use ActionBarCompat to create a basic Activity which displays action items. It covers inflating items from a menu resource, as well as adding an item in code.
ActionBarCompat-Styled
This sample shows you how to use ActionBarCompat with a customized theme. It utilizes a split action bar when running on a device with a narrow display, and shows three tabs.
ActiveNotifications
Notification Groups and the Notification Manager can be used together to simplify how users experience notifications. This sample demonstrates how the NotificationManager can tell you how many notifications your application is currently showing. It also shows how to manage the notifications as a group and introduce a summary for the group, when supported by the platform.
BasicNetworking
This sample demonstrates how to check network connectivity with Android APIs.
BeamLargeFiles
This sample demonstrates how to transfer large files via Android Beam. After the initial handshake over NFC, file transfer will take place over a secondary high-speed communication channel such as Bluetooth or WiFi Direct.
This feature requires Android 4.1 (Jelly Bean) or above. Unlike traditional Beam, your application will not receive an Intent on the receiving device. Instead, the system will save the file to disk and display a notification that the user can select to open the file using a standard ACTION_VIEW Intent.
BluetoothAdvertisements
Sample demonstrating how to advertise small amounts of data using the Bluetooth Low Energy API. Also demonstrates how to scan for those Advertisements. (requires 2 devices to see full operation)
BluetoothLeGatt
This sample demonstrates how to use the Bluetooth LE Generic Attribute Profile (GATT) to transmit arbitrary data between devices.
CardView
This sample demonstrates how to use CardView introduced in the support library in Android 5.0.
DirectShare
Sample demonstrating how to show some options directly in the list of share intent candidates.
DocumentCentricRecents
Sample demonstrating the basic usage of the new 'Document Centric Apps' API. It let's you create new documents in the system overview menu and persists its state through reboots.
HdrViewfinder
This demo implements a real-time high-dynamic-range camera viewfinder, by alternating the sensor's exposure time between two exposure values on even and odd frames, and then compositing together the latest two frames whenever a new frame is captured.
Vulkan API samples
Demonstrates basic usages of Vulkan APIs.
Notifications
This sample showcases the available notification styles on a device and wearable.
RecyclerView
Sample demonstrating the use of RecyclerView to layout elements with a LinearLayoutManager and with a GridLayoutManager. It also demonstrates how to handle touch events on elements.
AccelerometerPlay
Sample demonstrating how to use an accelerometer sensor as input for a physics-based view.
ActionBarCompat-ListPopupMenu
This sample shows how to display a pop up menu using PopupMenu from the v7 appcompat library.
ActionBarCompat-ShareActionProvider
This sample shows you how a provide a context-sensitive ShareActionProvider with ActionBarCompat, backwards compatible to API v7.
ActivityInstrumentation
This sample provides a basic example of using an InstrumentationTest to probe the internal state of an Activity.
ActivitySceneTransitionBasic
This sample shows how to use scene transitions from one Activity to another in Lollipop. Uses a combination of changeImageTransform and changeBounds to transition a grid of images to an Activity with a large image and detail text.
AdMob Banner
This sample demonstrates how to request and display an AdMob banner ad in an Android application. The app contains a single, "Hello World" activity with a banner at the bottom of its layout.
AdMob Interstitial
This sample demonstrates how to request and display an AdMob interstitial ad in an Android application. The code illustrates how to instantiate an InterstitialAd object, preload an interstitial, and then display it.
The app's UI contains a single activity with a countdown timer. When the timer reaches zero, the user can tap a "retry" button to display an interstitial and begin the countdown over again.
AdMob Native Ads Express
This sample demonstrates how to request and display an ad from AdMob Native Ads Express in an Android application. The app loads and displays a single ad at the bottom of its activity.
AdMob Native Advanced
This sample demonstrates how to request and display an ad from AdMob Native Ads Advanced in an Android application. The app displays an ad at the top of its activity, and offers a few checkboxes and a button you can use to request different native ad formats.
Advanced API Demos for Android
This is an advanced example application that covers a number of features in the AdMob and DoubleClick For Publishers APIs. It uses methods provided by the Mobile Ads SDK for targeting, sizing, exclusions, custom events, and more.
AdvancedImmersiveMode
Immersive Mode, added in Android 4.4, improves the "hide full screen" and "hide nav bar" modes by letting users swipe the bars in and out. This sample lets the user experiment with immersive mode by seeing how it interacts with some of the other UI flags related to full-screen apps.
AgendaData
Sample demonstrating sync of calendar events to a wearable by the press of a button.
AlwaysOn
A basic sample showing how to support ambient mode for native Android Wear apps.
AppRestrictionEnforcer
This sample demonstrates how to set restrictions to other apps as a profile owner. Use the AppRestrictionSchema sample to set restrictions.
AppRestrictionSchema
A basic app showing how to allow a device administrator to restrict user activities using the Android Device Administration API. The app exports a custom policy that enables or disables a UI control. Device Administration applications are able to enforce a specific value for this policy, as directed by enterprise administrators.
AppRestrictions
A sample that demonstrates the use of the App Restriction feature on devices with multiuser support
AppUsageStatistics
A basic app showing how to use App usage statistics API to let users collect statistics related to usage of the applications.
Audio-Echo
The sample demos how to use OpenSL ES to create a player and recorder in Android Fast Audio Path, and connect them to loopback audio. On most android devices, there is a optimized audio path that is tuned up for low latency purpose. The sample creates player/recorder to work in this highly optimized audio path(sometimes called native audio path, low latency path, or fast audio path). The application is validated against the following configurations: * Android L AndroidOne * Android M Nexus 5, Nexus 9 This sample uses the new Android Studio with CMake support, and shows how to use shared stl lib with android studio version 2.2.0, see CMakeLists.txt for details
BasicAccessibility
This sample demonstrates how to create an accessible application, using a mix of different widgets demonstrating different ways of adding accessibility markup to a UI.
BasicAndroidKeyStore
An advanced sample displaying the creation and usage of data integrity mechanisms
BasicContactables
This sample shows how to search for contacts, displaying a SearchView in the Action Bar for user input and implementing a query Cursor with CommonDataKinds.Contactables.
BasicGestureDetect
This sample detects gestures on a view and logs them. In order to try this sample out, try dragging or tapping the text.
BasicImmersiveMode
Sample demonstrating the use of immersive mode to hide the system and navigation bars for full screen applications.
BasicManagedProfile
This sample demonstrates basic functionalities of Managed Profile API introduced in Android 5.0 Lollipop. You can set up this app as a profile owner, and use this app to enable/disable apps in the newly created managed profile. You can also set restrictions to some apps, enable/disable Intent forwarding between profiles, and wipe out all the data associated with the profile.
BasicMediaDecoder
This sample shows how to use the MediaCoder to decode a video, use a TimeAnimator to sync the rendering commands with the system display frame rendering and finally render it to a TextureView.
BasicMediaRouter
This sample demonstrates the use of the MediaRouter API to display content on a secondary display. Use the "Media Route Action Item" in the ActionBar to select an output device. If your device supports Miracast wireless displays, you may need to enable "Wireless Display" functionality in the system settings. Secondary screen simulation can also be enabled from the "Developer Options".
Once connected, use the "Change Color" button to change the background color of the secondary screen.
BasicMultitouch
Sample demonstrates the use of MotionEvent properties to keep track of individual touches across multiple touch events.
BasicNotifications
A basic app showing how to display events in the system's notification bar using the NotificationCompat API. NotificationCompat API is used for compatibility with older devices, running Android 1.6 (Donut) (API level 4) or newer.
BasicRenderScript
This sample demonstrates using RenderScript to perform basic image manipulation. Specifically, it allows users to dynamically adjust the saturation for an image using a slider. A custom RenderScript kernel performs the saturation adjustment, running the computation on the device's GPU or other compute hardware as deemed appropriate by the system.
BasicSyncAdapter
This sample demonstrates using SyncAdapter to fetch background data for an app. It covers the creation of the required Service that the OS uses to initiate the background data sync as well as scheduling syncs with background data.
BasicTransition
A basic app showing how to use the Transition framework introduced in KitKat. The app shows radioboxes to select between different Scenes, and uses various ways to transition between them.
BatchStepSensor
Sample demonstrating how to set up SensorEventListeners for step detectors and step counters.
Bitmap Plasma
Bitmap Plasma is an Android sample that uses JNI to render a plasma effect in an Android Bitmap from C code.
This sample uses the new Android Studio CMake plugin with C++ support.
BluetoothChat
This sample shows how to implement two-way text chat over Bluetooth between two Android devices, using all the fundamental Bluetooth API capabilities.
BorderlessButtons
This sample demonstrates the borderless button styling from the Holo visual language. Styling is applied in the XML resource layout definitions, referecing the styling attributes from the Holo theme.
Camera2Basic
This sample demonstrates how to use basic functionalities of Camera2 API. You can learn how to iterate through characteristics of all the cameras attached to the device, display a camera preview, and take pictures.
Camera2Raw
This sample demonstrates using the Camera2 API to capture a JPEG and RAW sensor frame. Check the source code to see a typical example of how to display the camera preview; run auto-focus, auto-exposure metering, and auto-white-balance; capture a JPEG and RAW image for the same sensor frame; and save these into MediaStore for use in other applications.
Camera2Video
This sample shows how to record video using the new Camera2 API in Android Lollipop.
CardEmulation
This sample demonstrates how to emulate an NFC card, using the "host card emulation" feature added in Android 4.4. This sample makes the device appear as a loyalty card whenever the screen is on and the user taps their device on an appropriately configured NFC reader.
The "CardReader" sample can be used to read the loyalty card implemented in this sample.
CardReader
This sample demonstrates how to implement a low-level NFC card reader, for reading cards that do not contain NDEF or Android Beam data. This sample is designed to read the virtual loyalty card implemented in the "CardEmulation" sample.
In particular, this sample demonstrates how to disable Android Beam, select which AIDs the reader is interested, and establish communication with the card
ClippingBasic
A basic app showing how to clip on a View using ViewOutlineProvider interface, by which a View builds its outline, used for shadowing and clipping.
Confirm Credential
A sample that demonstrates how to use device credentials (PIN, Pattern, Password) in your app
CustomChoiceList
This sample demonstrates how to create custom checkable layouts, for use with ListView's choiceMode attribute.
CustomNotifications
This sample demonstrates notifications with custom content views. The use of collapsed and expanded notification views are shown.
CustomTransition
This sample shows how to implement a custom Transition extending the standard Transition class.
DataLayer
This sample demonstrates how to work with a WearableListenerService, to produce and consume DataEvents and effectively work with the DataLayer.
DelayedConfirmation
Demonstrates how to create a DelayedConfirmationView in your wearable app. In this sample, pressing a button on the phone app sends a message to the wearable to start a simple activity. This activity displays a DelayedConfirmationView that starts when the user presses "Start Timer." Then, callbacks are implemented on both the wearable and phone to show when the timer is selected or finishes. The activity on the wearable uses BoxInsetLayout to automatically apply appropriate margins based on whether the display is square or circular.
DeviceOwner
This sample demonstrates how to use some device owner features. As a device owner, you can configure global settings such as automatic time and timezone. You can mandate a specific launcher by preferred intent handler.
DirectorySelection
A basic app showing how to use Directory Selection API to let users select an entire directory subtree, which extends the Storage Access Framework introduced in Android 4.4 (API level 19).
DisplayingBitmaps
Sample demonstrating how to load large bitmaps efficiently off the main UI thread, caching bitmaps (both in memory and on disk), managing bitmap memory and displaying bitmaps in UI elements such as ViewPager and ListView/GridView.
DocumentCentricRelinquishIdentity
This sample shows how to relinquish identity to activities above it in the task stack.
DoneBar
This sample shows how to create a custom view in the ActionBar to show a done button, using 2 alternative layouts. This is well suited for simple data entry activities, where the only options for the user are to cancel or confirm the data changes.
DoubleClick Banner
This sample demonstrates how to request and display a DoubleClick For Publishers banner ad in an Android application. The app contains a single, "Hello World" activity with a banner at the bottom of its layout.
DoubleClick Custom Rendering
This sample demonstrates how to request and display an ad from DoubleClick for Publishers Custom Rendering in an Android application. The app displays an ad at the top of its activity, and offers a few checkboxes and a button you can use to request different native ad formats.
DoubleClick For Publishers Advanced Native Example
This project is an advanced native ads example intended to show how publishers might construct a list-based user experience (such as a news feed might have) that incorporates multiple native ad formats.
The project uses a single activity that maintains a ListView and an array of items. Most of these items are mocked listings for real estate, which stand in example application data. Placed among the sample listings are AdPlacement objects. These objects us AdFetchers to request ads from DFP Custom Rendering, construct NativeAdView instances to display them, and cache references to individual asset views in AdViewHolders.
Most of the AdPlacement classes handle a single type of ad. The MultiFormatAdPlacement, however, can request and display App Install, Content, and either of two custom template formats.
DoubleClick Interstitial
This sample demonstrates how to request and display a DoubleClick For Publishers interstitial ad in an Android application. The code illustrates how to instantiate a PublisherInterstitialAd object, preload an interstitial, and then display it.
The app's UI contains a single activity with a countdown timer. When the timer reaches zero, the user can tap a "retry" button to display an interstitial and begin the countdown over again.
DrawableTinting
Sample that shows applying tinting and color filters to Drawables both programmatically and as Drawable resources in XML.
Tinting is set on a nine-patch drawable through the "tint" and "tintMode" parameters. A color state list is referenced as the tint color, which defines colors for different states of a View (for example disabled/enabled, focused, pressed or selected).
Programmatically, tinting is applied to a Drawable through its "setColorFilter" method, with a reference to a color and a PorterDuff blend mode. The color and blend mode can be changed from the UI to see the effect of different options.
ElevationBasic
This sample demonstrates ways to move a view in the z-axis using setTranslationZ(). This method was introduced in API Level 21 ('Lollipop').
ElevationDrag
This sample demonstrates a drag and drop action on different shapes. Elevation and z-translation are used to render the shadows and the views are clipped using different Outlines.
ElizaChat
A basic sample showing how to add extensions to notifications on wearable using NotificationCompat.WearableExtender API by providing a chat experience.
Endless Tunnel
Endless Tunnel is a sample game that shows how to: - use the Android Studio C++ support - implement a game using Android native glue - implement joystick support, including robust DPAD navigation for non-touch screens
It is NOT the goal of this sample to show the best way to write the game logic, load resources, etc. The game itself was intentionally kept rudimentary in order to keep the focus on the Android Studio C++ integration. For example, this game contains textures and geometry hard-coded in code, which works for small demo games like this one, but doesn't scale well to real games.
This sample uses the new Android Studio CMake plugin with C++ support.
FindMyPhone
This sample application notifies you when you may have left your phone behind (specifically, when your companion and wearable disconnect). If you have misplaced your phone, but it is still connected to your wearable, you can also start an activity on the wearable to sound an alarm on your phone.
Flashlight
Sample demonstrating the use of an Activity in a wearable application. The sample uses the screen as a flashlight.
FloatingActionButtonBasic
This sample shows the two sizes of Floating Action Buttons and how to interact with them.
Geofencing
When the user enters the vicinity of the Android building (B44) or the Yerba Buena Gardens near the Moscone center in San Francisco, a notification silently appears on their wearable with an option to check in. This notification automatically disappears when they leave the area, and reappears the next time they are at one of these locations.
GridViewPager
Demonstrates how to implement a GridViewPager in your wearable app.
Hello GL2
Hello GL2 is an Android C++ sample that draws a triangle using GLES 2.0 API.
It uses JNI to do the rendering in C++ over a GLSurfaceView created from a regular Android Java Activity.
This sample uses the new Android Studio CMake plugin with C++ support.
Hello JNI
Hello JNI is an Android sample that uses JNI to call C code from a Android Java Activity.
This sample uses the new Android Studio CMake plugin with C++ support.
Hello JNI Callback
This sample is an Aadd-on to Hello JNI sample to demonstrate calling back to Java from C code - create a java class instance from C code - call java class static and non-static member functions
This sample uses the new Android Studio CMake plugin with C++ support.
Hello-libs
Hello-Libs is an Android sample that demos 3rd party native lib management with Android Studio
HorizontalPaging
This sample shows how to implement tabs, using Fragments and a ViewPager.
ImmersiveMode
One of the features introduced in KitKat is "immersive mode". Immersive mode gives the user the ability to show/hide the status bar and navigation bar with a swipe.To try, click the "Toggle immersive mode" button, then try swiping the bar in and out!
Interpolator
This sample demonstrates the use of animation interpolators and path animations for Material Design.
JumpingJack
A basic sample showing how to use the Gravity sensor on the wearable device by counting how many jumping jacks you have performed.
LNotifications
This sample demonstrates new features for notifications introduced in Android L. These features include heads-up notifications, visibility, people, category and priority metadata.
MediaBrowserService
This sample shows how to implement an audio media app that provides media library metadata and playback controls through a standard service. It exposes a simple music library through the new MediaBrowserService and provides MediaSession callbacks. This allows it to be used in Android Auto, for example. When not connected to a car, the app has a very simple UI that browses the media library and provides simple playback controls. When connected to Android Auto, the same service provides data and callback to the Android Auto UI in the same manner as it provides them to the local UI.
MediaEffects
This sample shows how to use the Media Effects APIs that were introduced in Android 4.0.
MediaRecorder
This sample uses the camera/camcorder as the A/V source for the MediaRecorder API. A TextureView is used as the camera preview which limits the code to API 14+. This can be easily replaced with a SurfaceView to run on older devices.
MediaRouter
Demonstrates how to create a custom media route provider.
MidiScope
Sample demonstrating how to use the MIDI API to receive and process MIDI signals coming from an attached device.
MidiSynth
Sample demonstrating how to use the MIDI API to receive and play MIDI messages coming from an attached input device (MIDI keyboard).
MultiWindowPlayground
This sample demonstrates the use of the multi-window API available in Android N. It shows the use of new Intent flags and AndroidManifest properties to define the multi-window behavior. Switch the sample app into multi-window mode to see how it affects the lifecycle and behavior of the app.
Native Activity
Native Activity is an Android sample that initializes a GLES 2.0 context and reads accelerometer data from C code using Native Activity.
This sample uses the new Android Studio CMake plugin with C++ support.
Native Ads Express RecyclerView
This sample demonstrates how to request and display ads from AdMob Native Ads Express in an Android application using the RecyclerView widget.
The RecyclerView widget is a more advanced and flexible version of ListView. This widget helps simplify the display and handling of large data sets by allowing the layout manager to determine when to reuse (recycle) item views that are no longer visible to the user. Recycling views improves performance by avoiding the creation of unnecessary views or performing expensive findViewByID() lookups.
Native Audio
Native Audio is an Android sample that plays and records sounds with the C++ OpenSLES API using JNI. The recorder / players created are not in fast audio path.
This sample uses the new Android Studio CMake plugin with C++ support.
Native Plasma
Native Plasma is an Android sample that renders a plasma effect in a Bitmap from C code using Native Activity.
This sample uses the new Android Studio CMake plugin with C++ support.
Navigation Drawer
This example illustrates a common usage of the DrawerLayout widget in the Android support library.
NetworkConnect
This sample demonstrates how to connect to the network and fetch raw HTML using HttpsURLConnection. AsyncTask is used to perform the fetch on a background thread.
NfcProvisioning
This sample demonstrates how to use NFC to provision a new device with a device owner. Device owner is a specialized type of device administrator that can control device security and configuration. This sample itself is not a device owner, but it is a programming app that sends NFC message to an unprovisioned peer device and tells it to set up the specified device owner app.
PdfRendererBasic
This sample demonstrates how to display PDF document on screen using the PdfRenderer introduced in Android 5.0 Lollipop.
PermissionRequest
This sample demonstrates how to use the PermissionRequest API to securely provide access to restricted system features (such as a camera or microphone) from within a WebView. In this example, a dialog is created to allow users to explicitly approve or reject each request.
Quiz
This sample uses Google Play Services Wearable Data APIs to communicate between applications on a phone and a paired wearable device. Users can create quiz questions on the phone, each of which has an associated DataItem. These DataItems are then received on the wearable, which displays them as notifications. Each notification contains the question as the first page, followed by answers as actions. When an answer is selected, the corresponding question's DataItem is updated, which allows the phone application to update the status of the question (i.e. did the user answer it correctly or not) and prompt the next question.
RenderScriptIntrinsic
RenderScriptIntrinsic sample that demonstrates how to use RenderScript intrinsics. Creates several RenderScript intrinsics and shows a filtering result with various parameters. Also shows how to extends RedioButton with StateListDrawable.
RepeatingAlarm
Introductory text that explains what the sample is intended to demonstrate. Edit in template-params.xml.
RevealEffectBasic
Sample demonstrating circular reveal effect. It covers creating an ViewAnimationUtils as well as defining the parameters of the circular reveal including starting position and radius.
RuntimePermissionsBasic
This basic sample shows runtime permissions available in the Android M and above. It shows how to use the new runtime permissions API to check and request permissions through the support library.
RuntimePermissionsWear
A sample that shows how you can handle remote data that requires permissions both on a wearable device and a mobile device.
Sample TV Channel App (TV Input) using TIF
This app is designed to show how to build live TV channel apps for Android TV using the TV Input Framework (TIF). The sample is a service that once installed, is recognized and run by the default TV app (e.g. Live Channels app).
San Angeles
San Angeles is an Android port of a demo that uses GLES C/API to render a procedural scene.
See the original README for more details about the original GLES port.
The sample demos: - ABI APK split
ScopedDirectoryAccess
This sample demonstrates how to use the Scoped Directory Access API introduced in Android N to easily access to specific directories such as Pictures, Downloads instead of requesting READ_EXTERNAL_STORAGE or WRITE_EXTERNAL_STORAGE in your manifest.
ScreenCapture
This sample demonstrates how to use Media Projection API to capture device screen in real time and show it on a SurfaceView.
Sensor-Graph
Sensor graph is a C++ Android sample that read current accelerometer values and draw them using OpenGL.
It demonstrate usage of the following Native C++ API: - Assets
This sample uses the new Android Studio CMake plugin with C++ support.
SkeletonWearableApp
This sample is a basic skeleton app which can be used as a starting point for wear development.
SlidingTabsBasic
A basic sample which shows how to use SlidingTabLayout to display a custom ViewPager title strip which gives continuous feedback to the user when scrolling.
SlidingTabsColors
A more advanced sample which shows how to use SlidingTabLayout to display a custom ViewPager title strip, with custom coloring for each tab.
SpeedTracker
Sample demonstrates recording location and speed with a Wear device in mind. Location is retrieved via FusedLocatinProvider which retrieves coordinates from the phone or Wear depending on whether the phone is disconnected or not and whether the Wear device has a GPS chip.
StorageClient
Using the OPEN_DOCUMENT intent, a client app can access a list of Document Providers on the device, and choose a file from any of them.
StorageProvider
This sample shows how to implement a simple documents provider using the storage access framework available in Android 4.4.
SwipeRefreshLayoutBasic
A basic sample which shows how to use SwipeRefreshLayout to add the 'swipe-to-refresh' gesture to a View, enabling the ability to trigger a refresh from swiping down on the view. In this sample the View which can be refreshed is a ListView.
SwipeRefreshListFragment
A sample which shows how to use SwipeRefreshLayout to add 'swipe-to-refresh' gesture to a ListView, enabling the ability to trigger a refresh from swiping down on that view.
SwipeRefreshMultipleViews
A sample which shows how to use SwipeRefreshLayout to add the 'swipe-to-refresh' gesture to a layout with multiple children, enabling the ability to trigger a refresh from swiping down on the visible view. In this sample, SwipeRefreshLayout contains a scrollable GridView, along with a TextView empty view.
SynchronizedNotifications
A basic sample showing how to use simple or synchronized notifications. This allows users to dismiss events from either their phone or wearable device simultaneously.
TV Leanback Support Library sample - Videos by Google

This sample is a Videos By Google app, designed to run on an Android TV device (such as the Nexus Player), which demonstrates how to use the Leanback Support library which enables you to easily develop beautiful Android TV apps with a user-friendly UI that complies with the UX guidelines of Android TV.
Teapots
Teapots is an collection of Android C++ samples that uses a Teapot rendering to demostrate Android NDK platform features: - classic-teapot: Rendering classic teapot mesh using GLES 2.0 API and NativeActivity. - more-teapots: Rendering multiple instances of Classic Teapot with GLES 3.0 Instance Rendering - Choreographer-30fps: demonstrates multiple frame rate throttoling techniques based on API level using Chreographer API and EGL Android presentation time extension.
This sample uses the new Android Studio CMake plugin with C++ support.
TextLinkify
This sample illustrates how links can be added to a TextView. This can be done either automatically by setting the "autoLink" property or explicitly.
TextSwitcher
This sample illustrates the use of a TextSwitcher to display animations for text changes.
Timer
This simple wearable app allows the user to set a countdown timer. It runs independently on the wearable with no phone connection.
Trivial Drive
Sample for In-App Billing version 3
Universal Music Player
This sample shows how to implement an audio media app that works across multiple form factors and provide a consistent user experience on Android phones, tablets, Android Auto, Android Wear, Android TV and Google Cast devices.
WEBPs
Webp is an Android sample including a small app to demo usage of webp in Native Activityview: - rotate decoding 3 webp images and load them into on-screen buffer. Decoding is in its own thread
This sample uses the new Android Studio CMake plugin.
WatchViewStub
This sample demonstrates how to specify different layouts for round and rectangular screens.
WearComplicationProvidersTestSuite
Complication Test Suite is a set of complication providers that provide dummy data and it can be used to test how different types of complications render on a watch face.
WearNotifications
Sample demonstrates best practices for using NotificationStyle Notifications (Inbox, BigPicture, BigText, and Messaging) for both Mobile apps and native/local Android Wear apps. It also covers Notifications on Wear 1.+ and Wear 2.0.
WearSpeakerSample
A sample that shows how you can record voice using the microphone on a wearable and play the recorded voice or an mp3 file, if the wearable device has a built-in speaker.
This sample doesn't have any companion phone app so you need to install this directly on your watch (using "adb").
WearVerifyRemoteApp
Sample demonstrates best practices for checking if connected mobile device has your app installed from an Android Wear 2.+ standalone app and the other way around.
XYZTouristAttractions
This sample aims to be as close to a real world example of a mobile and Wear app combination as possible. It has a more refined design and also provides a practical example of how a mobile app would interact and communicate with its wear counterpart.
The app itself is modeled after a hypothetical tourist attractions app that notifies the user when they are in close proximity to notable points of interest.
The Wear component shows tourist attraction images and summary information, and provides quick actions for nearby tourist attractions in a GridViewPager UI component.
gles3jni
gles3jni is an Android C++ sample that demonstrates how to use OpenGL ES 3.0 from JNI/native code.
The OpenGL ES 3.0 rendering path uses a few new features compared to the OpenGL ES 2.0 path: - Instanced rendering and vertex attribute divisor to reduce the number of draw calls and uniform changes. - Vertex array objects to reduce the number of calls required to set up vertex attribute state on each frame. - Explicit assignment of attribute locations, eliminating the need to query assignments.
This sample uses the new Android Studio CMake plugin with C++ support.
