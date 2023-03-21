const apiURL    = 'https://restcountries.eu/rest/v2/alpha/',
countries       = ['AFG','ALB','DZA','ASM','AND','AGO','ATA','ARG','ARM','AUS','AUT','AZE','BHS','BHR','BGD','BLR','BEL','BMU','BTN','BOL','BIH','BWA','BRA','IOT','BGR','KHM','CMR','CAN','CPV','CAF','TCD','CHL','CHN','CXR','COL','COG','COD','CRI','HRV','CUB','CYP','CZE','DNK','DMA','DOM','ECU','EGY','SLV','EST','ETH','FJI','FIN','FRA','GUF','GMB','GEO','DEU','GHA','GIB','GRC','GRL','GTM','GGY','GIN','GNB','GUY','HTI','HMD','VAT','HND','HKG','HUN','ISL','IND','IDN','IRN','IRQ','IRL','IMN','ISR','ITA','JAM','JPN','JEY','JOR','KAZ','KEN','KIR','PRK','KOR','XKX','KWT','KGZ','LAO','LVA','LBN','LTU','LUX','MAC','MKD','MDG','MWI','MYS','MDV','MLI','MLT','MHL','MTQ','MRT','MUS','MYT','MEX','FSM','MDA','MCO','MNG','MNE','MSR','MAR','MOZ','MMR','NAM','NRU','NPL','NLD','NCL','NZL','NIC','NER','NGA','NOR','OMN','PAK','PLW','PSE','PAN','PNG','PRY','PER','PHL','PCN','POL','PRT','PRI','QAT','SRB','REU','ROU','RUS','SMR','STP','SAU','SEN','SGP','SXM','SVK','SVN','SLB','SOM','ZAF','SGS','SSD','ESP','LKA','SDN','SWZ','SWE','CHE','SYR','TWN','TJK','TZA','THA','TON','TTO','TUN','TUR','TKM','UGA','UKR','ARE','GBR','USA','UMI','URY','UZB','VUT','VEN','VNM','YEM','ZMB','ZWE'],

items_Container = document.querySelector('.content__items'),
selecFilter     = document.querySelector('select'),
optionFilter    = document.querySelectorAll('option'),
inputSearch     = document.querySelector('input'),
darkModeToggle  = document.querySelector('.header-darkmode'),
content         = document.querySelector('.content'),
itemView        = document.querySelector('.itemView'),
itemViewContent = document.querySelector('.itemView__content'),
backButton      = document.querySelector('.backbutton'),
body            = document.body;

const createItem  = async( country ) => {

    for(let country of countries){

        let resp = await fetch( `${ apiURL }${country}` );
        resp = await resp.json();

        const div = document.createElement('div');
        div.classList.add('content__items-item');
        div.id = country;


        const html = `
            <img src="${ resp.flag }" alt="country flag">
            <div class="content__items-item-description">
                <p class="name"><b>${ resp.name }</b></p>
                <p class="population"><b>Population: </b>${ resp.population.toLocaleString() }</p>
                <p class="region"><b>Region: </b>${ resp.region }</p>
                <p class="capital"><b>Capital: </b>${ resp.capital }</p>
            </div>
        `;

        div.innerHTML = html;
        items_Container.append(div);

    }

    console.log('Done1');

}

const deleteRepeatedSelect = async(  ) => {

    let array = [],
    arrayUnique = [];

    for(let i = 0; i < countries.length - 1; i++){
        let resp = await fetch( `${ apiURL }${countries[i]}` );
        resp = await resp.json();
        let region = resp.region;
        array.push(region);
    }

    array.forEach( (repeated) => {
        if( !arrayUnique.includes(repeated) ){
            arrayUnique.push(repeated);
        }
    } )

    arrayUnique.forEach( (aU) => {
        const option = document.createElement('option');
        option.setAttribute('value', `${aU}`);

        const html = `
        ${aU}`;

        option.innerHTML = html;
        selecFilter.append(option);
    } )

    console.log('Done2');
}

const filterRegion = (value) => {
    item = document.querySelectorAll('.content__items-item');
    
    if(value != 'all'){
        for(let elem of item){
            if(!elem.textContent.includes(value)){
                elem.classList.add('hideItem');
            } else if (elem.textContent.includes(value)) {
                elem.classList.remove('hideItem');
            }
        }
    } else {
        for(let elem of item){
            elem.classList.remove('hideItem');
        }
    }
}

const searchOnInput = (  ) => {
    let value = inputSearch.value.toLowerCase();
    value = value.charAt(0).toUpperCase() + value.slice(1);
    console.log(value);
    const pName    = document.querySelectorAll('.name');

    if(value != ''){
        for(let elem of pName){
            if(!elem.textContent.includes(value)){
                elem.parentElement.parentElement.classList.add('hideItem');
            } else if (elem.textContent.includes(value)) {
                elem.parentElement.parentElement.classList.remove('hideItem');
            }
        }
    } else {
        for(let elem of pName){
            elem.parentElement.parentElement.classList.remove('hideItem');
        }
    }
}

const addListener = async() => {
    const itemI = document.querySelectorAll('.content__items-item');
    for(const item of itemI){
        item.addEventListener('click', openDetails)
    }
}

const openDetails = async(item) => {
    let i = item.target;
    while( !i.classList.contains("content__items-item") ){
        i = i.parentElement;
    }

    let id = i.getAttribute('id');

    // Creando HTML
    let resp = await fetch( `${ apiURL }${id}` );
        resp = await resp.json();

        const html = `
            <img src="${ resp.flag }" alt="Country flag">
            <div class="itemView__content-data">
                <h2>${ resp.name }</h2>
                <div class="itemView__content-data-description">
                    <div class="itemView__content-data-description1">
                        <p><b>Native Name: </b>${ resp.nativeName }</p>
                        <p><b>Poblation: </b>${ resp.population.toLocaleString() }</p>
                        <p><b>Region: </b>${ resp.region }</p>
                        <p><b>Sub-region: </b>${ resp.subregion }</p>
                        <p><b>Capital: </b>${ resp.capital }</p>
                    </div>
                    <div class="itemView__content-data-description1">
                        <p><b>Top Level Domain: </b>${ resp.topLevelDomain }</p>
                        <p><b>Currencies: </b>${ resp.currencies[0].name }</p>
                        <p><b>Languages: </b>${ resp.languages[0].name }</p>
                    </div>
                </div>
                <p class="border"><b>Border Countries:</b></p>
                
            </div>
        `;

        itemViewContent.innerHTML = html;

        await getBorders( resp.borders );
    
        content.classList.add('hide');
        itemView.classList.remove('hide');
}

const getBorders = async( bordersArray ) => {
    console.log(bordersArray);
    const buttonContainer = document.querySelector('.itemView__content-data');

    if( bordersArray.length == 0 ) {
        button = document.createElement('button');
        button.classList.add('borderBtn');
        button.innerHTML = 'None';
        buttonContainer.append(button);
    } else if( (bordersArray.length - 1) == 1 ){
        for(let i = 0; i <= 1; i++){
            button = document.createElement('button');
            button.classList.add('borderBtn');
            button.innerHTML = await executeFetch( bordersArray[i].toLowerCase() );
            buttonContainer.append(button);
        }
    } else {
        for(let i = 0; i <= 2; i++){
            button = document.createElement('button');
            button.classList.add('borderBtn');
            button.innerHTML = await executeFetch( bordersArray[i].toLowerCase() );
            buttonContainer.append(button);
        }
    }
}

const executeFetch = async( country ) => {
    let resp = await fetch( `${ apiURL }${country}` );
    let { name } = await resp.json();
    return name;
}

darkModeToggle.addEventListener('click', () => {
    const darkModeDiv = document.querySelector('.header-darkmode');
    
    body.classList.toggle('darkMode');
    darkModeDiv.classList.add('darkModeSpin');
    
    if( darkModeDiv.children[0].classList.contains('fas') ){
        darkModeDiv.children[0].classList.remove('fas');
        darkModeDiv.children[0].classList.add('far');
    } else {
        darkModeDiv.children[0].classList.add('fas');
        darkModeDiv.children[0].classList.remove('far');
    }

    setTimeout(() => {
        darkModeDiv.classList.remove('darkModeSpin');
    }, 500);
});

backButton.addEventListener('click', () => {
    content.classList.remove('hide');
    itemView.classList.add('hide');
})

inputSearch.addEventListener('keyup', searchOnInput)

selecFilter.addEventListener('change', () => filterRegion(selecFilter.value));

createItem().then( deleteRepeatedSelect )
            .then( addListener );
