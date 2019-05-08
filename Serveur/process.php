<?php
$file='messagefeed.txt';
$handle=fopen($file,'a' );
$fullmsg=$_GET['u']." : ".$_GET['msg'];
fwrite($handle, $fullmsg);
?>