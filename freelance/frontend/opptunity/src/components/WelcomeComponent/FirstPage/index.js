
import profileImg from './profile_image.jpg'
import './style.css'
const FirstPageComponent = () => {
    return (

<div>
    <h2>Welcome to our community</h2>
    <p>Clarity gives you the blocks & components you need to create a truly professional website.</p>
    <div className="ratings">
    <span>⭐⭐⭐⭐⭐</span>
    <p>"We love Landingfolio! Our designers were using it for their projects, so we already knew what kind of design they want."</p>
    <div className="contact">
        <img  className= "test" src={profileImg}></img>
    <div className="test">
        <p>Devon Lane</p>
        <p>Co-Founder, Design.co</p>
    </div>
    </div>
    </div>
</div> 
    )
}
export default FirstPageComponent
