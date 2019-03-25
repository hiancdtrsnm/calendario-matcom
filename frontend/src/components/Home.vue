<template>
    <div id="home">
        <div class="row">
            <div class="col">
                <div class="dropdown mb-0">
                    <button class="btn btn-light dropdown-toggle" type="button" id="career_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" style="width: auto">
                        Carrera
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" >
                        <div class="input-group m-2 " v-for="it in careers" :key="it.name">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" @click="updateData('m_careers', it.val)">
                                <span class="ml-2" id="basi00-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col ml-2">
                <div class="dropdown mb-0">
                    <button class="btn btn-light dropdown-toggle" type="button" id="year_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" style="width: auto">
                        Año
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" >
                        <div class="input-group m-2 " v-for="it in years" :key="it.name">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" @click="updateData('m_years', it.val)">
                                <span class="ml-2" id="basi01-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-0">
                    <button class="btn btn-light dropdown-toggle" type="button" id="semester_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" style="width: auto">
                        Semestre
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" >
                        <div class="input-group m-2 " v-for="it in semesters" :key="it.name">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" @click="updateData('m_semesters', it.val)">
                                <span class="ml-2" id="basi02-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-0">
                    <button class="btn btn-light dropdown-toggle" type="button" id="asignaturas_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" @click="tmp()">
                        Asignaturas
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);" >
                        <div class="input-group m-2 " v-for="it in marked" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basic-">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-0">
                    <button class="btn btn-light dropdown-toggle" type="button" id="grupos_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Grupos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in groups" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basi7-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-0">
                    <button class="btn btn-light dropdown-toggle" type="button" id="locales_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Locales
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in locals" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basi3-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-0">
                    <button class="btn btn-light dropdown-toggle" type="button" id="resources_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Recursos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in resources" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basi1-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-0">
                    <button class="btn btn-light dropdown-toggle" type="button" id="tipos_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Tipos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in tags" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basi5-addon3">{{it.text}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <button class="btn btn-block btn-outline-dark" @click="makeQuery">
                    Filtrar
                </button>
            </div>
        </div>
        <div class="row">
            <div class="card-body mt-0" @click.stop style="width: 200px">
                <div class="row ml-5">
                    <div class="col-1">
                        <h1 class="h5 text-dark mt-1">Desde:</h1>
                    </div>
                    <div class="col-5">
                        <datetime  type="datetime" :phrases="phrases" v-model="datetimeStart" ></datetime>
                    </div>
                    <div class="col-1">
                        <h1 class="h5 text-dark mt-1 ">Hasta:</h1>
                    </div>
                    <div class="col-5">
                        <datetime type="datetime" :phrases="phrases" v-model="datetimeEnd"></datetime>
                    </div>
                </div>
            </div>
        </div>
        <full-calendar :events="events" :config="config" @event-selected="eventSelected"></full-calendar>
    </div>
</template>

<script>
    import { FullCalendar } from 'vue-full-calendar';
    import 'fullcalendar/dist/locale/es';
    import { Datetime } from 'vue-datetime';
    import { Settings } from 'luxon';

    Settings.defaultLocale = 'es';

    export default {
        name: "Home",
        components: {
            Datetime,
            FullCalendar
        },
        data () {
            return {
                careers: [],
                m_careers: {},
                years: [],
                m_years: {},
                semesters: [],
                m_semesters: {},
                courses: [],
                resources: [],
                locals: [],
                tags: [],
                groups: [],
                events: [],
                marked:  [],
                config: {
                    schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
                    defaultView: 'agendaWeek',
                    locale: 'es',
                    editable: false,
                    selectable: false,
                    navLinks: true,
                    header: {
                        left: 'prev,next today',
                        center: 'title',
                        right: 'month,agendaWeek,agendaDay,listWeek'
                    },
                    scrollTime: '08:00:00',
                    allDaySlot: false
                },
                datetimeStart: '',
                datetimeEnd: '',
                phrases: {ok: 'Aceptar',cancel: 'Cancelar'}
            }
        },
        methods: {
            loadAll () {
                this.loadFromCourses();
                this.loadFrom('groups');
                this.loadFrom('locals');
                this.loadFrom('resources');
                this.loadFrom('tags');
                // this.loadAdditionals('year',this.courses,this.years);
                // this.loadAdditionals('semester',this.courses,this.semesters);
            },
            loadFrom(arg) {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state[arg].getData(token).then(result => {
                    this[arg] = this.$store.state[arg].data;
                });
            },
            loadFromCourses() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.courses.getData(token).then(result => {
                    this.courses = this.$store.state.courses.data;
                    this.courses.forEach(item => {
                        if(item['career'] !== null) {
                            let insert = true;
                            for(let i = 0; i < this.careers.length; i++){
                                if( this.careers[i].name === item['career']){
                                    insert = false;
                                    break;
                                }
                            }
                            if(insert === true){
                                this.careers.push({ name: item['career'], val:item['career'] });
                            }
                        }
                        if(item['year'] !== 0){
                            let insert = true;
                            for(let i = 0; i < this.years.length; i++){
                                if( this.years[i].name === item['year']){
                                    insert = false;
                                    break;
                                }
                            }
                            if(insert === true){
                                this.years.push({ name: item['year'], val: item['year'] });
                            }
                        }
                        if(item['semester'] !== 0){
                            let insert = true;
                            for(let i = 0; i < this.semesters.length; i++){
                                if( this.semesters[i].name === 'Semestre ' + item['semester']){
                                    insert = false;
                                    break;
                                }
                            }
                            if(insert === true){
                                this.semesters.push({ name: 'Semestre ' + item["semester"], val: item['semester'] });
                            }
                        }
                        else{
                            let insert = true;
                            for(let i = 0; i < this.semesters.length; i++){
                                if( this.semesters[i].name === 'Anual'){
                                    insert = false;
                                    break;
                                }
                            }
                            if(insert === true){
                                this.semesters.push({ name: 'Anual', val: 0 });
                            }
                        }

                    });
                    // let tmp = new Set(this.careers);
                    // let tmp1 = new Set(this.years);
                    // let tmp2 = new Set(this.semesters);
                    // this.careers = tmp;
                    // this.years = tmp1;
                    // this.semesters = tmp2;
                    // let tmp4 = [];
                    // this.courses.forEach(this.getMarkedYears(tmp4,this.m_years));
                    // console.log(tmp4);
                    //console.log(this.careers);
                });
            },
            tmp(){
                this.marked = this.getAllMarked(this.m_careers,this.m_years, this.m_semesters, this.courses);
                // console.log(Object.keys(this.m_careers).length);
                // console.log(this.m_years);
                // console.log(this.m_semesters);
                // let tmp = [];
                //this.courses.forEach(this.getMarkedStuff(tmp,this.m_careers,'career'));
                // this.courses.forEach(this.getMarkedCareers(tmp,this.m_careers));
                // console.log(tmp);
                // console.log(this.getAllMarked(this.m_careers,this.m_years, this.m_semesters, this.courses));
                // console.log(this.verifyTrue(this.m_careers));
            },
            updateData(list, val){
                if(this[list][val] === true){
                    this[list][val] = false;
                }
                else{
                    this[list][val] = true;
                }
            },
            loadAdditionals(arg, list){
                let tmp = [];
                for(let i = 0; i < list.lenght; i++){
                    tmp.push(list[i][arg]);
                    console.log(list[i][arg]);
                }
                return tmp;
            },
            getMarkedData(to) {
                return (item => {
                    if (item.hasOwnProperty('isMarked') && item.isMarked) {
                        to.push(item.id);
                    }
                });
            },
            getMarkedStuff(to, years, val){
                return(item => {
                    for(let i = 0; i < Object.keys(years).length; i++){
                        let tmp = parseInt(Object.keys(years)[i]);
                        if(item[val] == tmp && years[tmp]){
                            to.push(item);
                        }
                    }
                });
            },
            getMarkedCareers(to, career){
                return(item => {
                    for(let i = 0; i < Object.keys(career).length; i++){
                        let tmp = Object.keys(career)[i];
                        // console.log(career);
                        if(item['career'] == tmp && career[tmp]){
                            to.push(item);
                        }
                    }
                });
            },
            getAllMarked(careers, years, semesters, cources){
                let tmp1 = [];
                if(Object.keys(years).length > 0 && this.verifyTrue(years)){
                    cources.forEach(this.getMarkedStuff(tmp1, years, 'year'));
                }
                else{
                    tmp1 = cources;
                }
                let tmp2 = [];
                if(Object.keys(semesters).length > 0 && this.verifyTrue(semesters)){
                    tmp1.forEach(this.getMarkedStuff(tmp2, semesters, 'semester'));
                }
                else{
                    tmp2 = tmp1;
                }
                let tmp3 = [];
                if(Object.keys(careers).length > 0 && this.verifyTrue(careers)){
                    tmp2.forEach(this.getMarkedCareers(tmp3, careers));
                }
                else{
                    tmp3 = tmp2;
                }
                // tmp2 = Object.keys(careers).length > 0 ? cources.forEach(this.getMarkedStuff(tmp1, years, 'year')) : cources;
                return tmp3;
            },
            verifyTrue(list){
                let result = false;
                for(let i = 0; i < Object.keys(list).length; i++){
                    let tmp = Object.keys(list)[i];
                    result |= list[tmp];
                }
                return result;
            },
            makeQuery() {
                this.m_careers = {};
                this.m_semesters = {};
                this.m_years = {};
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                let toSendTags = [];
                let toSendCourses = [];
                let toSendGroups = [];
                let toSendLocals = [];
                let toSendResources = [];
                let toSendUsers = [];
                let toSendStartDate = null;
                let toSendEndDate = null;
                this.courses.forEach(this.getMarkedData(toSendCourses));
                this.tags.forEach(this.getMarkedData(toSendTags));
                this.groups.forEach(this.getMarkedData(toSendGroups));
                this.locals.forEach(this.getMarkedData(toSendLocals));
                this.resources.forEach(this.getMarkedData(toSendResources));
                if (this.datetimeStart !== '') {
                    toSendStartDate = this.datetimeStart;
                }
                if (this.datetimeEnd !== '') {
                    toSendEndDate = this.datetimeEnd;
                }
                this.$store.state.query.makeQuery(token, toSendCourses, toSendGroups, toSendLocals, toSendTags, toSendResources, toSendUsers, toSendStartDate, toSendEndDate)
                    .then(result => {
                        if (result === true) {
                            this.events = this.$store.state.query.data;
                            this.events.forEach(event => {
                                event.color = '#428bca';
                                event.textColor = '#ffffff';
                            });
                        }
                        this.loadAll();
                    });
            },
            eventSelected(event, jsEvent, view) {
                this.$router.push({name: 'eventPage', params: {eventId: event.id}});
            },
            setMarked(list, name){
                for(let i = 0; i < list.length; i++){
                    if(list[i].name === name){
                        let tmp = list[i].isMarked;
                        list[i].isMarked = !tmp;
                        break;
                    }
                }
            }
        },
        created() {
            this.makeQuery();
        }
    }
</script>

<style>
@import '~fullcalendar/dist/fullcalendar.min.css';
@import '~vue-datetime/dist/vue-datetime.css';

.fc-event {
    cursor: pointer;
}

.fc-list-item {
    cursor: pointer;
}
</style>
