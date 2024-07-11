class Video {
    constructor(title, uploader, time){
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }
    watch(){
        console.log(`${this.uploader} watched all ${this.time} seconds of "${this.title}"`)
    }
}

const mrBeast = new Video('Look what 100 desperate people will do for money', 'MrBeast', 1200);
mrBeast.watch();
const JRE = new Video('Mr. Pseudoscientist: Aliens, UFOs, Drugs and the CIA');
