function msToTime(duration) {
  var milliseconds = parseInt((duration % 1000) / 100),
    seconds = Math.floor((duration / 1000) % 60),
    minutes = Math.floor((duration / (1000 * 60)) % 60);

  minutes = (minutes < 10) ? "0" + minutes : minutes;
  seconds = (seconds < 10) ? "0" + seconds : seconds;

  return minutes + ":" + seconds;
}
if (document.querySelector("#video_player")) {
				new FWDUVPlayer({
					//main settings
					instanceName:"player_white",
					parentId:"video_player",
          playlistsId:"video_playlists",
      		mainFolderPath:"/static",
      		skinPath:"images/video_white/",
					displayType:"responsive",
					useVectorIcons:"yes",
					fillEntireVideoScreen:"no",
					fillEntireposterScreen:"yes",
					goFullScreenOnButtonPlay:"no",
					playsinline:"yes",
					initializeOnlyWhenVisible:"no",
					privateVideoPassword:"428c841430ea18a70f7b06525d4b748a",
					youtubeAPIKey:'AIzaSyCGBNj8zTFSq8JPWH2dkFPQ5WD5VBJbXAs',
					useHEXColorsForSkin:"no",
					normalHEXButtonsColor:"#FF0000",
					selectedHEXButtonsColor:"#000000",
					facebookAppId:"213684265480896",
					googleAnalyticsTrackingCode:"",
					useResumeOnPlay:"no",
					useDeepLinking:"yes",
					showPreloader:"yes",
					preloaderBackgroundColor:"#000000",
					preloaderFillColor:"#FFFFFF",
					addKeyboardSupport:"yes",
					autoScale:"yes",
					showButtonsToolTip:"yes",
					stopVideoWhenPlayComplete:"no",
					playAfterVideoStop:"no",
					autoPlay:"no",
					loop:"no",
					shuffle:"no",
					showErrorInfo:"yes",
					maxWidth:1170,
					maxHeight:659,
					volume:.8,
					buttonsToolTipHideDelay:1.5,
					backgroundColor:"#eeeeee",
					videoBackgroundColor:"#000000",
					posterBackgroundColor:"#000000",
					buttonsToolTipFontColor:"#FFFFFF",
					//logo settings
					showLogo:"yes",
					hideLogoWithController:"yes",
					logoPosition:"topRight",
					logoLink:"http://www.webdesign-flash.ro/",
					logoMargins:10,
					//playlists/categories settings
					showPlaylistsSearchInput:"yes",
					usePlaylistsSelectBox:"yes",
					showPlaylistsButtonAndPlaylists:"yes",
					showPlaylistsByDefault:"no",
					thumbnailSelectedType:"opacity",
					startAtPlaylist:0,
					buttonsMargins:15,
					thumbnailMaxWidth:350,
					thumbnailMaxHeight:350,
					horizontalSpaceBetweenThumbnails:40,
					verticalSpaceBetweenThumbnails:40,
					inputBackgroundColor:"#333333",
					inputColor:"#000000",
					//playlist settings
					showPlaylistButtonAndPlaylist:"yes",
					playlistPosition:"right",
					showPlaylistByDefault:"yes",
					showPlaylistName:"yes",
					showSearchInput:"yes",
					showLoopButton:"yes",
					showShuffleButton:"yes",
					showPlaylistOnFullScreen:"no",
					showNextAndPrevButtons:"yes",
					showThumbnail:"yes",
					forceDisableDownloadButtonForFolder:"yes",
					addMouseWheelSupport:"yes",
					startAtRandomVideo:"no",
					stopAfterLastVideoHasPlayed:"no",
					addScrollOnMouseMove:"no",
					randomizePlaylist:'no',
					folderVideoLabel:"VIDEO ",
					playlistRightWidth:320,
					playlistBottomHeight:380,
					startAtVideo:0,
					maxPlaylistItems:50,
					thumbnailWidth:71,
					thumbnailHeight:71,
					spaceBetweenControllerAndPlaylist:1,
					spaceBetweenThumbnails:1,
					scrollbarOffestWidth:8,
					scollbarSpeedSensitivity:.5,
					playlistBackgroundColor:"#eeeeee",
					playlistNameColor:"#000000",
					thumbnailNormalBackgroundColor:"#ffffff",
					thumbnailHoverBackgroundColor:"#eeeeee",
					thumbnailDisabledBackgroundColor:"#eeeeee",
					searchInputBackgroundColor:"#F3F3F3",
					searchInputColor:"#888888",
					youtubeAndFolderVideoTitleColor:"#000000",
					folderAudioSecondTitleColor:"#999999",
					youtubeOwnerColor:"#919191",
					youtubeDescriptionColor:"#919191",
					mainSelectorBackgroundSelectedColor:"#000000",
					mainSelectorTextNormalColor:"#000000",
					mainSelectorTextSelectedColor:"#FFFFFFF",
					mainButtonBackgroundNormalColor:"#FFFFFF",
					mainButtonBackgroundSelectedColor:"#000000",
					mainButtonTextNormalColor:"#000000",
					mainButtonTextSelectedColor:"#FFFFFF",
					//controller settings
					showController:"yes",
					showControllerWhenVideoIsStopped:"yes",
					showNextAndPrevButtonsInController:"no",
					showRewindButton:"yes",
					showPlaybackRateButton:"yes",
					showVolumeButton:"yes",
					showTime:"yes",
					showQualityButton:"yes",
					showInfoButton:"yes",
					showDownloadButton:"yes",
					showShareButton:"yes",
					showEmbedButton:"yes",
					showChromecastButton:"no",
					showFullScreenButton:"yes",
					disableVideoScrubber:"no",
					showScrubberWhenControllerIsHidden:"yes",
					showMainScrubberToolTipLabel:"yes",
					showDefaultControllerForVimeo:"no",
					repeatBackground:"yes",
					controllerHeight:43,
					controllerHideDelay:3,
					startSpaceBetweenButtons:10,
					spaceBetweenButtons:10,
					scrubbersOffsetWidth:2,
					mainScrubberOffestTop:14,
					timeOffsetLeftWidth:5,
					timeOffsetRightWidth:3,
					timeOffsetTop:0,
					volumeScrubberHeight:80,
					volumeScrubberOfsetHeight:12,
					timeColor:"#919191",
					youtubeQualityButtonNormalColor:"#919191",
					youtubeQualityButtonSelectedColor:"#000000",
					scrubbersToolTipLabelBackgroundColor:"#000000",
					scrubbersToolTipLabelFontColor:"#FFFFFF",
					//advertisement on pause window
					aopwTitle:"Advertisement",
					aopwWidth:400,
					aopwHeight:240,
					aopwBorderSize:6,
					aopwTitleColor:"#000000",
					//subtitle
					subtitlesOffLabel:"Subtitle off",
					//popup add windows
					showPopupAdsCloseButton:"yes",
					//embed window and info window
					embedAndInfoWindowCloseButtonMargins:15,
					borderColor:"#CDCDCD",
					mainLabelsColor:"#000000",
					secondaryLabelsColor:"#444444",
					shareAndEmbedTextColor:"#777777",
					inputBackgroundColor:"#c0c0c0",
					inputColor:"#333333",
					//loggin
					isLoggedIn:"yes",
					playVideoOnlyWhenLoggedIn:"yes",
					loggedInMessage:"Please login to view this video.",
					//audio visualizer
					audioVisualizerLinesColor:"#ff9f00",
					audioVisualizerCircleColor:"#FFFFFF",
					//lightbox settings
					lightBoxBackgroundOpacity:.6,
					lightBoxBackgroundColor:"#000000",
					//sticky on scroll
					stickyOnScroll:"no",
					stickyOnScrollShowOpener:"yes",
					stickyOnScrollWidth:"700",
					stickyOnScrollHeight:"394",
					//sticky display settings
					showOpener:"yes",
					showOpenerPlayPauseButton:"yes",
					verticalPosition:"bottom",
					horizontalPosition:"center",
					showPlayerByDefault:"yes",
					animatePlayer:"yes",
					openerAlignment:"right",
					mainBackgroundImagePath:"content/minimal_skin_dark/main-background.png",
					openerEqulizerOffsetTop:-1,
					openerEqulizerOffsetLeft:3,
					offsetX:0,
					offsetY:0,
					//playback rate / speed
					defaultPlaybackRate:1, //0.25, 0.5, 1, 1.25, 1.2, 2
					//cuepoints
					executeCuepointsOnlyOnce:"no",
					//annotations
					showAnnotationsPositionTool:"no",
					//ads
					openNewPageAtTheEndOfTheAds:"no",
					adsButtonsPosition:"left",
					skipToVideoText:"You can skip to video in: ",
					skipToVideoButtonText:"Skip Ad",
					adsTextNormalColor:"#888888",
					adsTextSelectedColor:"#000000",
					adsBorderNormalColor:"#AAAAAA",
					adsBorderSelectedColor:"#000000",
					//a to b loop
					useAToB:"yes",
					atbTimeBackgroundColor:"transparent",
					atbTimeTextColorNormal:"#888888",
					atbTimeTextColorSelected:"#FFFFFF",
					atbButtonTextNormalColor:"#888888",
					atbButtonTextSelectedColor:"#FFFFFF",
					atbButtonBackgroundNormalColor:"#FFFFFF",
					atbButtonBackgroundSelectedColor:"#000000",
					//thumbnails preview
					thumbnailsPreviewWidth:196,
					thumbnailsPreviewHeight:110,
					thumbnailsPreviewBackgroundColor:"#000000",
					thumbnailsPreviewBorderColor:"#666",
					thumbnailsPreviewLabelBackgroundColor:"#666",
					thumbnailsPreviewLabelFontColor:"#FFF",
					// context menu
					showContextmenu:'yes',
					showScriptDeveloper:"no",
					contextMenuBackgroundColor:"#ebebeb",
					contextMenuBorderColor:"#ebebeb",
					contextMenuSpacerColor:"#CCC",
					contextMenuItemNormalColor:"#888888",
					contextMenuItemSelectedColor:"#000",
					contextMenuItemDisabledColor:"#BBB"
				});

FWDUVPUtils.onReady(function(){
    video_player.addListener(FWDUVPlayer.READY, video_onReady);
    video_player.addListener(FWDUVPlayer.PLAY, video_onPlay);
});
}
function music_onReady(){console.log("Аудио плеер готов");}
function video_onReady(){console.log("Видео плеер готов");}


function video_onPlay(){
    console.log("Воспроизводится видео №: " + video_player.getVideoId());
    music_player.pause();
}
