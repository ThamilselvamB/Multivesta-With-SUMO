import vesta.quatex.*;
import vesta.mc.*;
public class _1911077509stepsAtTime extends QuatexExp {
	private double x;
	public _1911077509stepsAtTime(double x){
		this.x=x;
	}

	public QuatexExp eval(State s){
		if ( s.rval(0) >= x ){
			return new QuatexValue( s.rval(1) );
		} else {
			return new _1911077509stepsAtTime(x);		}
	}

}

