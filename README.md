### Jojo Stands Api

This API shows some information of users and stands throughout the Anime series. Some information that is retrieve from this API includes `Stand Image`, `Stand Type`, `User Image` and much more.
This API was built using [Flask](https://flask.palletsprojects.com/en/2.0.x/). All the information was collected from [Jojo WiKi](https://jojowiki.com).

---
1. [Endpoints](#endpoint)
2. [Query String Parameters](#query-string-parameters)
3. [Example of http response](#example-of-http-response)
4. [Issues](#issues)
---

### Endpoints

#### Main Endpoint

This is the main endpoint https://jojoapi.herokuapp.com **all other end urls should be prepend to this main url**.

Currently, this returns all the information of 3 seasons of the Anime, these are `Stardust Crusaders`, `Diamond Is Unbreakable` and `Golden Wind`.


#### Other Endpoints

These returns the information specifi to each serie. Others such as `Stone Ocean`, `Steel Ball Run` and `Jojolion` will be added in the future

    * /StardustCrusaders
    * /DiamondIsUnbreakable
    * /GoldenWind

#### Query String Parameters

Parameters that are passed to the URL query string, for example:

    * https://jojoapi.herokuapp.com?eye_color=insert_eye_color_to_search
    * https://jojoapi.herokuapp.com?eye_color=insert_stand_type_to_search

This will display all the users with the specific characteristics. **Only one parameter can be pass**
Some of the parameters are:
    - eye_color
    - stand_type
    - hair_color
    - gender.

#### Example of http response

![](https://im.ge/i/Xj5jOp)

#### Issues

If you find any bugs or would like to implement any features feel free to open an [issue](https://github.com/ItzSylex/JojoAPI/issues/new)

---

I am currently re-writing the API and updating it
