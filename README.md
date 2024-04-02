# UNESCO World Heritage Maping

This application visualizes UNESCO World Heritage Sites on an interactive map. Users can explore cultural and natural heritage sites, obtain information, and directly visit UNESCO's official website to learn more. I used dataset from UNESCO's official website. This data set was .xls.

## Data Preparation 
On offical website has 4 file type. For data preparation firstly convert file to .json. After this cleaning dataset with js.

## Edit map title and default text
Go to `index.html` to edit the map title, introductory text, and footer, which always appears in the sidebar when users click on different places.

Enter map initial center and zoom level in `settings.js`:
```
// Map's initial center, and zoom level
const mapCenter = [41.65, -72.7];
const mapZoom = 9;
```

In the maps legend, the label *Themes* corresponds to *Groups* in the Google Sheet template. To edit this label in the map, go to `script.js` and modify the label "Themes" in this line:

```
L.control.layers({}, groups, {collapsed: false}).addTo(map);
$('.leaflet-control-layers-overlays').prepend('<h3 class="mt0 mb1 f5 black-30">Themes</h3>');
```

## Assign the same place to 2 or more categories
If a place needs to belong to two or more groups (also known as themes or categories),
duplicate its row as many times as needed, and each time modifying its
*Group* column only.

## Add custom thumbnail photo icons
Each place can have 1 custom thumbnail photo icon. Make a copy of your main image, then use a photo editor to crop and reduce the size to 64 x 64 pixels square, and upload into your GitHub repo and enter the pathname into the Google Sheets template, such as: `media/frog-bridge-icon.jpg`.

In `settings.js`, you can modify the photo icon size as desired, such as 40 x 40 pixels, to squeeze multiple icons on a crowded map.

```
// Marker icon height and width
const iconHeight = 40;
const iconWidth = 40;
```
## Share web links with URL hash

This feature enables you to share a particular place with others on social media, because when the map is loaded initially,
it activates the place from hash if it exists instead of centering
on default `mapCenter` (as defined in `settings.js`).

## Application Views
 - All categories are selected.
   ![image](https://github.com/bugracntp/UNESCO-world-heritage/assets/66384957/cd889f86-5a41-4cbf-a164-9dc3771dd7cf)
- Only one category selected
  ![image](https://github.com/bugracntp/UNESCO-world-heritage/assets/66384957/55f603fa-7ce1-4e8d-8499-f87641a6db36)
- When select a location from map
  ![image](https://github.com/bugracntp/UNESCO-world-heritage/assets/66384957/a1b54fdd-148c-43ec-834e-68a8e9312191)



