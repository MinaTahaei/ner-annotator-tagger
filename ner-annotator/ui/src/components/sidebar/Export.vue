<template>
  <div class="my-2">
    <button class="button is-danger" @click="generateJSONExport()">
      Export Annotations
    </button>
    <button class="button is-primary" style="margin-left:50px" @click="showSample()">
        ? 
        </button>
  </div>
</template>
<script>
import {mapState} from "vuex";
import Swal from "sweetalert2";
export default {
  name: "Export",
  computed: {
    ...mapState(["annotations", "classes"]),
  },
  methods: {
    generateJSONExport() {
      if(this.$store.state.taggerName === "" | this.$store.state.taggerName === undefined){
        Swal.fire("Enter your name","","warning");
        return;
      }
      const filename = this.$store.state.fileName + ".json";
      const output = {
        'taggerName':this.$store.state.taggerName,
        "classes": this.classes.map(c => c.name),
        "annotations": this.annotations
      }

      const jsonStr = JSON.stringify(output);
      console.log(jsonStr)
      let element = document.createElement("a");
      element.setAttribute(
        "href",
        "data:text/plain;charset=utf-8," + encodeURIComponent(jsonStr)
      );
      element.setAttribute("download", filename);

      element.style.display = "none";
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    },
    showSample(){
      const filename = "test.json";
      const output = {
        'taggerName':'user',
        "classes": ["PER", "GEN", "DATE", "CITY", "LOC", "SKILL", "INS", "DEGREE", "MAJOR", "ORG", "POS", "CER", "ENGLEVEL"],
        "annotations": [["﻿ به نام خدا سوابق كارى، علمى و پژوهشى (رزومه) نام و نام خانوادگى: سمانه كرلو (Samaneh Korlou) شماره همراه : ٠٩٣٨٧٩٦٤٣٦٤ تولد : ١٣٧٠ وضعيت تاهل: مجرد محل سكونت: تهران پست الكترونيك: Samaneh_k70 @ yahoo.com • تحصيلات ◦ كارشناسى مهندسى صنايع، دانشگاه خواجه نصير، رتبه ٢٥٩ منطقه دو كشورى كنكور كارشناسى ◦ كارشناسى ارشد مهندسى صنايع-سيستم دانشگاه تهران، ، رتبه ارشد٣٦، گرايش سيستم • سوابق پژوهشى ◦ پروژه كارشناسى: طراحى ايجاد صنايع، بررسى واحدهاى توليدكننده نايلون و نايلكس واحدهاى كشاورزى ◦ موضوع پايان نامه كارشناسى ارشد: طراحى زنجيره تامين سوخت زيستى تحت شرايط عدم قطعيت (حل و مدلسازى با گمز و متلب و بهينه سازى استوار) ◦ انجام پروژه درس احتمال و كنترل كيفيت پروژه درسى، با نرمافزار مينى تب o انجام پروژه درس كنترل پروژه، مربوط به يك ساختمان ده طبقه با نرم افزار MSPo انجام پروژه درس روش توليد،كارخانه ايندامين سايپا و بازديد از خط توليد ◦ انجام پروژه طراحى محيط گرافيكى (GUI) براى اطلاعات دانش آموزان يك مدرسه با كمك نرم MATLAB افزار • سوابق كارى ▪ شركت رويال ، پلاست كارآموزى، انجام پروژه طراحى ايجاد صنايع، مطالعه خط توليد و تهيه گزارش از خط توليد با مقايسه با خط توليد هاى ديگر ▪ دانشگاه تهران، امور دفترى، سرپرستى تيم ها و انجام كارهاى ادارى و پذيرش و بيمهاى و تهيه و آماده كردن مدارك مربوطه ▪ شركت بهبود سيستم، ارزياب، تهيه گزارش هاى آمارى، شركت زير مجموعه اى از كانون فرهنى آموزش (قلم چى) ، انجام امور ادارى و ثبت نام و سايت و تهيه گزارشات مربوطه، تهيه گزارشات مديريتى با اكسل • توانمندى هاى تخصصى • اكسل مسلط (مسلط به استفاده از توابع vlookup) وmatchو indexو ...) ، رسم نمودار ها و Pivot tableها، آشنابه محيط برنامه نويسى اكسل و آشنا به تهيه داشبورهاى مديريتى) o آشنا به طرز تهيه داشبورد هاى مديريتى در اكسل (نمودارآدمك، گيج، آبشارى و ...) o آشنا با زبان برنامه نويسى ويژوال بيسيك در اكسل (VBA) o ورد و پاورپوينت و اكسس مسلط o آشنا با زبان انگليسى در سطح خوب o در حال تقويت مهارت اكسل مهندسى صنايع و كنترل پروژه و كنترل كيفيت o در حال تقويت مهارت پايگاه داده SQL • در حال تقويت مهارت تحليل سيستمى و تهيه گزارشهاى مديريتى در بخشهاى مختلف مهندسى صنايع • در حال تقويت مهارت زبان تخصصى مهندسى صنايع o آشنا با مهارت تحقيق و جستجو در اينترنت و تايپ پيشرفته • آشنايى با نرم افزار MATLAB و كد نويسى و آشنايى با الگوريتمهاى فراابتكارى × دورهها و گواهينامهها • دوره آشنايى با اكسل در مهندسى صنايع، محل برگزارى دانشگاه خواجه نصير طوسى o دوره آنلاين اكسل مقدماتى و پيشرفته، موسسه Lyndao دوره آنلاين كد نويسى در اكسل (VBA) ، فرادرس • دوره مهندسى فروش و بازاريابى،محل برگزارى وزارت صنعت ومعدن o دوره آشنايى با ايزو evand، محل برگزارى دانشگاه تهران • علاقهمندىها ◦ لجستيك و زنجيره تامين o انرژى هاى نو o علم داده • توضيحات ◦ هدف شغلى من پيگيرى كارهاى محوله و پيشرفت در كار و وظيفه شغلى محوله به بهترين شكل ممكن مىباشد. ◦ از ويژگىهاى مهم فردى من اينكه خودآموز خوبى هستم كه در كار و شغل به خوبى نمايان مىشود. • ويژگىهاى فردى ▪ ريزبين و منظم هستم و به پايان رساندن و كيفيت كارها برايم مهم است. ▪ روحيه كار تيمى را دارم. ▪ روحيه كارمندى دارم. ▪ پيگير، با اشتياق، انعطاف پذى و سخت كوش هستم. ▪ ESTJ، MBTI نتيجه تست",{"entities":[[141,145,"PER"],[2060,2068,"LOC"]]}]]
      }

      const jsonStr = JSON.stringify(output);
      console.log(jsonStr)
      let element = document.createElement("a");
      element.setAttribute(
        "href",
        "data:text/plain;charset=utf-8," + encodeURIComponent(jsonStr)
      );
      element.setAttribute("download", filename);

      element.style.display = "none";
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    }
  },
};
</script>
