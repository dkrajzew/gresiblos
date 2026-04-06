<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head><title>A sample blog</title></head>

 <body>
<?php
function params_get($which) {
  if(isset($_GET[$which])) {
    $v = $_GET[$which];
    if($v!="") return $v;
  }
  return null;
}

function tinyReplace($format, $values) {
  $ret = $format;
  foreach ($values as $key => $value) {
    if(!is_string($value)) {
       continue;
    }
    $ret = str_replace("%".$key."%", $value, $ret);
  }
  return $ret;
}

function writeItemsAsList($items, $format) {
  echo("<ul class=\"entrylist\">\n");
  foreach ($items as $e) {
    echo(tinyReplace($format, $e));
  }
  echo("</ul>\n");
}

function cmp1($a, $b) {
  return $a->idate<$b->idate;
}

function sortItems($items, $field, $dir=SORT_DESC) {
  usort($items, "cmp1");
  return $items;
}

function filterItemsByTopic($items, $value) {
  $ret = array();
  $key = "topics";
  foreach ($items as $ekey => $row) {
    $found = 0;
    foreach ($row->$key as $topic) {
      $ttopic = trim($topic);
      if($ttopic==$value) {
        $found = 1;
      }
    }
    if($found==1) {
      $ret[$ekey] = $row;
    }
  }
  return $ret;
}

// this is only responsible for showing lists or menus
// the blog entries themselves exist as pre-built static pages
$toShow = params_get("show"); // "items", "topics"
if($toShow==null) $toShow = "items";
$db = file_get_contents("entries.json");
$entries = json_decode($db);
foreach ($entries as $entry) {
  $t1 = strptime($entry->date, '%Y-%m-%d %H:%M:%S');
  $entry->idate = mktime($t1['tm_hour'], $t1['tm_min'], 0, $t1['tm_mon']+1, $t1['tm_mday'], $t1['tm_year']+1900);
}
if($toShow=="topics") {
  // show (all) topics
  echo("<h1>Covered Topics</h1>\n");
  $topics = array();
  foreach ($entries as $entry) {
    foreach ($entry->topics as $topic) {
      $ttopic = trim($topic);
      $topics[$ttopic] = array("title"=>$ttopic);
    }
  }
  ksort($topics);
  writeItemsAsList($topics, "<li><a href=\"index.php?topic=%title%\">%title%</a></li>\n");
} else {
  $topicFilter = params_get("topic");
  if($topicFilter!=null) {
    $entries = filterItemsByTopic($entries, $topicFilter);
  }
  $entries = sortItems($entries, "idate", SORT_DESC);
  if($topicFilter==null) {
    echo("<h1>Most recent entries</h1>\n");
  } else {
    if(count($entries)==0) {
      echo("<h1>No entries for this topic found.</h1>\n");
    } else {
      echo("<h1>Most recent entries for topic '".$topicFilter."'</h1>\n");
    }
  }
  writeItemsAsList($entries, "<li><a href=\"%filename%\">%title%</a> (%date%)<br/>%abstract% (<a href=\"%filename%\">read more</a>)</li>\n");
}
?>
 </body>
</html>


