# --- AUTO-GENERATED FILE ---

from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from pyffmpeg.node import Stream, FilterMultiOutput


class GeneratedFiltersMixin:
    """
    Mixin class containing auto-generated filter methods.
    This class should be inherited by the Stream class.
    """

    def a3dscope(
        self,
        rate: str = None,
        r: str = None,
        size: str = None,
        s: str = None,
        fov: float = None,
        roll: float = None,
        pitch: float = None,
        yaw: float = None,
        xzoom: float = None,
        yzoom: float = None,
        zzoom: float = None,
        xpos: float = None,
        ypos: float = None,
        zpos: float = None,
        length: int = None,
    ) -> "Stream":
        """Convert input audio to 3d scope video output."""
        return self._apply_filter(
            filter_name="a3dscope",
            inputs=[self],
            named_arguments={
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "fov": fov,
                "roll": roll,
                "pitch": pitch,
                "yaw": yaw,
                "xzoom": xzoom,
                "yzoom": yzoom,
                "zzoom": zzoom,
                "xpos": xpos,
                "ypos": ypos,
                "zpos": zpos,
                "length": length,
            },
        )[0]

    def aap(
        self,
        desired_stream: "Stream",
        order: int = None,
        projection: int = None,
        mu: float = None,
        delta: float = None,
        out_mode: Literal["i", "d", "o", "n", "e"] | int = None,
        precision: Literal["auto", "float", "double"] | int = None,
    ) -> "Stream":
        """Apply Affine Projection algorithm to first audio stream."""
        return self._apply_filter(
            filter_name="aap",
            inputs=[self, desired_stream],
            named_arguments={
                "order": order,
                "projection": projection,
                "mu": mu,
                "delta": delta,
                "out_mode": out_mode,
                "precision": precision,
            },
        )[0]

    def abench(self, action: Literal["start", "stop"] | int = None) -> "Stream":
        """Benchmark part of a filtergraph."""
        return self._apply_filter(
            filter_name="abench",
            inputs=[self],
            named_arguments={
                "action": action,
            },
        )[0]

    def abitscope(
        self,
        rate: str = None,
        r: str = None,
        size: str = None,
        s: str = None,
        colors: str = None,
        mode: Literal["bars", "trace"] | int = None,
        m: Literal["bars", "trace"] | int = None,
    ) -> "Stream":
        """Convert input audio to audio bit scope video output."""
        return self._apply_filter(
            filter_name="abitscope",
            inputs=[self],
            named_arguments={
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "colors": colors,
                "mode": mode,
                "m": m,
            },
        )[0]

    def acompressor(
        self,
        level_in: float = None,
        mode: Literal["downward", "upward"] | int = None,
        threshold: float = None,
        ratio: float = None,
        attack: float = None,
        release: float = None,
        makeup: float = None,
        knee: float = None,
        link: Literal["average", "maximum"] | int = None,
        detection: Literal["peak", "rms"] | int = None,
        level_sc: float = None,
        mix: float = None,
    ) -> "Stream":
        """Audio compressor."""
        return self._apply_filter(
            filter_name="acompressor",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "mode": mode,
                "threshold": threshold,
                "ratio": ratio,
                "attack": attack,
                "release": release,
                "makeup": makeup,
                "knee": knee,
                "link": link,
                "detection": detection,
                "level_sc": level_sc,
                "mix": mix,
            },
        )[0]

    def acontrast(self, contrast: float = None) -> "Stream":
        """Simple audio dynamic range compression/expansion filter."""
        return self._apply_filter(
            filter_name="acontrast",
            inputs=[self],
            named_arguments={
                "contrast": contrast,
            },
        )[0]

    def acopy(self) -> "Stream":
        """Copy the input audio unchanged to the output."""
        return self._apply_filter(
            filter_name="acopy", inputs=[self], named_arguments={}
        )[0]

    def acrossfade(
        self,
        crossfade1_stream: "Stream",
        nb_samples: str = None,
        ns: str = None,
        duration: str = None,
        d: str = None,
        overlap: bool = None,
        o: bool = None,
        curve1: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int = None,
        c1: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int = None,
        curve2: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int = None,
        c2: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int = None,
    ) -> "Stream":
        """Cross fade two input audio streams."""
        return self._apply_filter(
            filter_name="acrossfade",
            inputs=[self, crossfade1_stream],
            named_arguments={
                "nb_samples": nb_samples,
                "ns": ns,
                "duration": duration,
                "d": d,
                "overlap": overlap,
                "o": o,
                "curve1": curve1,
                "c1": c1,
                "curve2": curve2,
                "c2": c2,
            },
        )[0]

    def acrossover(
        self,
        split: str = None,
        order: Literal[
            "2nd", "4th", "6th", "8th", "10th", "12th", "14th", "16th", "18th", "20th"
        ]
        | int = None,
        level: float = None,
        gain: str = None,
        precision: Literal["auto", "float", "double"] | int = None,
    ) -> "FilterMultiOutput":
        """Split audio into per-bands streams."""
        return self._apply_dynamic_outputs_filter(
            filter_name="acrossover",
            inputs=[self],
            named_arguments={
                "split": split,
                "order": order,
                "level": level,
                "gain": gain,
                "precision": precision,
            },
        )

    def acrusher(
        self,
        level_in: float = None,
        level_out: float = None,
        bits: float = None,
        mix: float = None,
        mode: Literal["lin", "log"] | int = None,
        dc: float = None,
        aa: float = None,
        samples: float = None,
        lfo: bool = None,
        lforange: float = None,
        lforate: float = None,
    ) -> "Stream":
        """Reduce audio bit resolution."""
        return self._apply_filter(
            filter_name="acrusher",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "bits": bits,
                "mix": mix,
                "mode": mode,
                "dc": dc,
                "aa": aa,
                "samples": samples,
                "lfo": lfo,
                "lforange": lforange,
                "lforate": lforate,
            },
        )[0]

    def acue(
        self, cue: str = None, preroll: str = None, buffer: str = None
    ) -> "Stream":
        """Delay filtering to match a cue."""
        return self._apply_filter(
            filter_name="acue",
            inputs=[self],
            named_arguments={
                "cue": cue,
                "preroll": preroll,
                "buffer": buffer,
            },
        )[0]

    def addroi(
        self,
        x: str = None,
        y: str = None,
        w: str = None,
        h: str = None,
        qoffset: str = None,
        clear: bool = None,
    ) -> "Stream":
        """Add region of interest to frame."""
        return self._apply_filter(
            filter_name="addroi",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "qoffset": qoffset,
                "clear": clear,
            },
        )[0]

    def adeclick(
        self,
        window: float = None,
        w: float = None,
        overlap: float = None,
        o: float = None,
        arorder: float = None,
        a: float = None,
        threshold: float = None,
        t: float = None,
        burst: float = None,
        b: float = None,
        method: Literal["add", "a", "save", "s"] | int = None,
        m: Literal["add", "a", "save", "s"] | int = None,
    ) -> "Stream":
        """Remove impulsive noise from input audio."""
        return self._apply_filter(
            filter_name="adeclick",
            inputs=[self],
            named_arguments={
                "window": window,
                "w": w,
                "overlap": overlap,
                "o": o,
                "arorder": arorder,
                "a": a,
                "threshold": threshold,
                "t": t,
                "burst": burst,
                "b": b,
                "method": method,
                "m": m,
            },
        )[0]

    def adeclip(
        self,
        window: float = None,
        w: float = None,
        overlap: float = None,
        o: float = None,
        arorder: float = None,
        a: float = None,
        threshold: float = None,
        t: float = None,
        hsize: int = None,
        n: int = None,
        method: Literal["add", "a", "save", "s"] | int = None,
        m: Literal["add", "a", "save", "s"] | int = None,
    ) -> "Stream":
        """Remove clipping from input audio."""
        return self._apply_filter(
            filter_name="adeclip",
            inputs=[self],
            named_arguments={
                "window": window,
                "w": w,
                "overlap": overlap,
                "o": o,
                "arorder": arorder,
                "a": a,
                "threshold": threshold,
                "t": t,
                "hsize": hsize,
                "n": n,
                "method": method,
                "m": m,
            },
        )[0]

    def adecorrelate(self, stages: int = None, seed: str = None) -> "Stream":
        """Apply decorrelation to input audio."""
        return self._apply_filter(
            filter_name="adecorrelate",
            inputs=[self],
            named_arguments={
                "stages": stages,
                "seed": seed,
            },
        )[0]

    def adelay(self, delays: str = None, all: bool = None) -> "Stream":
        """Delay one or more audio channels."""
        return self._apply_filter(
            filter_name="adelay",
            inputs=[self],
            named_arguments={
                "delays": delays,
                "all": all,
            },
        )[0]

    def adenorm(
        self,
        level: float = None,
        type: Literal["dc", "ac", "square", "pulse"] | int = None,
    ) -> "Stream":
        """Remedy denormals by adding extremely low-level noise."""
        return self._apply_filter(
            filter_name="adenorm",
            inputs=[self],
            named_arguments={
                "level": level,
                "type": type,
            },
        )[0]

    def aderivative(self) -> "Stream":
        """Compute derivative of input audio."""
        return self._apply_filter(
            filter_name="aderivative", inputs=[self], named_arguments={}
        )[0]

    def adrawgraph(
        self,
        m1: str = None,
        fg1: str = None,
        m2: str = None,
        fg2: str = None,
        m3: str = None,
        fg3: str = None,
        m4: str = None,
        fg4: str = None,
        bg: str = None,
        min: float = None,
        max: float = None,
        mode: Literal["bar", "dot", "line"] | int = None,
        slide: Literal["frame", "replace", "scroll", "rscroll", "picture"] | int = None,
        size: str = None,
        s: str = None,
        rate: str = None,
        r: str = None,
    ) -> "Stream":
        """Draw a graph using input audio metadata."""
        return self._apply_filter(
            filter_name="adrawgraph",
            inputs=[self],
            named_arguments={
                "m1": m1,
                "fg1": fg1,
                "m2": m2,
                "fg2": fg2,
                "m3": m3,
                "fg3": fg3,
                "m4": m4,
                "fg4": fg4,
                "bg": bg,
                "min": min,
                "max": max,
                "mode": mode,
                "slide": slide,
                "size": size,
                "s": s,
                "rate": rate,
                "r": r,
            },
        )[0]

    def adrc(
        self,
        transfer: str = None,
        attack: float = None,
        release: float = None,
        channels: str = None,
    ) -> "Stream":
        """Audio Spectral Dynamic Range Controller."""
        return self._apply_filter(
            filter_name="adrc",
            inputs=[self],
            named_arguments={
                "transfer": transfer,
                "attack": attack,
                "release": release,
                "channels": channels,
            },
        )[0]

    def adynamicequalizer(
        self,
        threshold: float = None,
        dfrequency: float = None,
        dqfactor: float = None,
        tfrequency: float = None,
        tqfactor: float = None,
        attack: float = None,
        release: float = None,
        ratio: float = None,
        makeup: float = None,
        range: float = None,
        mode: Literal["listen", "cutbelow", "cutabove", "boostbelow", "boostabove"]
        | int = None,
        dftype: Literal["bandpass", "lowpass", "highpass", "peak"] | int = None,
        tftype: Literal["bell", "lowshelf", "highshelf"] | int = None,
        auto: Literal["disabled", "off", "on", "adaptive"] | int = None,
        precision: Literal["auto", "float", "double"] | int = None,
    ) -> "Stream":
        """Apply Dynamic Equalization of input audio."""
        return self._apply_filter(
            filter_name="adynamicequalizer",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "dfrequency": dfrequency,
                "dqfactor": dqfactor,
                "tfrequency": tfrequency,
                "tqfactor": tqfactor,
                "attack": attack,
                "release": release,
                "ratio": ratio,
                "makeup": makeup,
                "range": range,
                "mode": mode,
                "dftype": dftype,
                "tftype": tftype,
                "auto": auto,
                "precision": precision,
            },
        )[0]

    def adynamicsmooth(
        self, sensitivity: float = None, basefreq: float = None
    ) -> "Stream":
        """Apply Dynamic Smoothing of input audio."""
        return self._apply_filter(
            filter_name="adynamicsmooth",
            inputs=[self],
            named_arguments={
                "sensitivity": sensitivity,
                "basefreq": basefreq,
            },
        )[0]

    def aecho(
        self,
        in_gain: float = None,
        out_gain: float = None,
        delays: str = None,
        decays: str = None,
    ) -> "Stream":
        """Add echoing to the audio."""
        return self._apply_filter(
            filter_name="aecho",
            inputs=[self],
            named_arguments={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
            },
        )[0]

    def aemphasis(
        self,
        level_in: float = None,
        level_out: float = None,
        mode: Literal["reproduction", "production"] | int = None,
        type: Literal["col", "emi", "bsi", "riaa", "cd", "50fm", "75fm", "50kf", "75kf"]
        | int = None,
    ) -> "Stream":
        """Audio emphasis."""
        return self._apply_filter(
            filter_name="aemphasis",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "mode": mode,
                "type": type,
            },
        )[0]

    def aeval(
        self, exprs: str = None, channel_layout: str = None, c: str = None
    ) -> "Stream":
        """Filter audio signal according to a specified expression."""
        return self._apply_filter(
            filter_name="aeval",
            inputs=[self],
            named_arguments={
                "exprs": exprs,
                "channel_layout": channel_layout,
                "c": c,
            },
        )[0]

    def aexciter(
        self,
        level_in: float = None,
        level_out: float = None,
        amount: float = None,
        drive: float = None,
        blend: float = None,
        freq: float = None,
        ceil: float = None,
        listen: bool = None,
    ) -> "Stream":
        """Enhance high frequency part of audio."""
        return self._apply_filter(
            filter_name="aexciter",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "amount": amount,
                "drive": drive,
                "blend": blend,
                "freq": freq,
                "ceil": ceil,
                "listen": listen,
            },
        )[0]

    def afade(
        self,
        type: Literal["in", "out"] | int = None,
        t: Literal["in", "out"] | int = None,
        start_sample: str = None,
        ss: str = None,
        nb_samples: str = None,
        ns: str = None,
        start_time: str = None,
        st: str = None,
        duration: str = None,
        d: str = None,
        curve: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int = None,
        c: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int = None,
        silence: float = None,
        unity: float = None,
    ) -> "Stream":
        """Fade in/out input audio."""
        return self._apply_filter(
            filter_name="afade",
            inputs=[self],
            named_arguments={
                "type": type,
                "t": t,
                "start_sample": start_sample,
                "ss": ss,
                "nb_samples": nb_samples,
                "ns": ns,
                "start_time": start_time,
                "st": st,
                "duration": duration,
                "d": d,
                "curve": curve,
                "c": c,
                "silence": silence,
                "unity": unity,
            },
        )[0]

    def afftdn(
        self,
        noise_reduction: float = None,
        nr: float = None,
        noise_floor: float = None,
        nf: float = None,
        noise_type: Literal["white", "w", "vinyl", "v", "shellac", "s", "custom", "c"]
        | int = None,
        nt: Literal["white", "w", "vinyl", "v", "shellac", "s", "custom", "c"]
        | int = None,
        band_noise: str = None,
        bn: str = None,
        residual_floor: float = None,
        rf: float = None,
        track_noise: bool = None,
        tn: bool = None,
        track_residual: bool = None,
        tr: bool = None,
        output_mode: Literal["input", "i", "output", "o", "noise", "n"] | int = None,
        om: Literal["input", "i", "output", "o", "noise", "n"] | int = None,
        adaptivity: float = None,
        ad: float = None,
        floor_offset: float = None,
        fo: float = None,
        noise_link: Literal["none", "min", "max", "average"] | int = None,
        nl: Literal["none", "min", "max", "average"] | int = None,
        band_multiplier: float = None,
        bm: float = None,
        sample_noise: Literal["none", "start", "begin", "stop", "end"] | int = None,
        sn: Literal["none", "start", "begin", "stop", "end"] | int = None,
        gain_smooth: int = None,
        gs: int = None,
    ) -> "Stream":
        """Denoise audio samples using FFT."""
        return self._apply_filter(
            filter_name="afftdn",
            inputs=[self],
            named_arguments={
                "noise_reduction": noise_reduction,
                "nr": nr,
                "noise_floor": noise_floor,
                "nf": nf,
                "noise_type": noise_type,
                "nt": nt,
                "band_noise": band_noise,
                "bn": bn,
                "residual_floor": residual_floor,
                "rf": rf,
                "track_noise": track_noise,
                "tn": tn,
                "track_residual": track_residual,
                "tr": tr,
                "output_mode": output_mode,
                "om": om,
                "adaptivity": adaptivity,
                "ad": ad,
                "floor_offset": floor_offset,
                "fo": fo,
                "noise_link": noise_link,
                "nl": nl,
                "band_multiplier": band_multiplier,
                "bm": bm,
                "sample_noise": sample_noise,
                "sn": sn,
                "gain_smooth": gain_smooth,
                "gs": gs,
            },
        )[0]

    def afftfilt(
        self,
        real: str = None,
        imag: str = None,
        win_size: int = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
        overlap: float = None,
    ) -> "Stream":
        """Apply arbitrary expressions to samples in frequency domain."""
        return self._apply_filter(
            filter_name="afftfilt",
            inputs=[self],
            named_arguments={
                "real": real,
                "imag": imag,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
            },
        )[0]

    def afir(
        self,
        *streams: "Stream",
        dry: float = None,
        wet: float = None,
        length: float = None,
        gtype: Literal["none", "peak", "dc", "gn", "ac", "rms"] | int = None,
        irnorm: float = None,
        irlink: bool = None,
        irgain: float = None,
        irfmt: Literal["mono", "input"] | int = None,
        maxir: float = None,
        response: bool = None,
        channel: int = None,
        size: str = None,
        rate: str = None,
        minp: int = None,
        maxp: int = None,
        nbirs: int = None,
        ir: int = None,
        precision: Literal["auto", "float", "double"] | int = None,
        irload: Literal["init", "access"] | int = None,
    ) -> "Stream":
        """Apply Finite Impulse Response filter with supplied coefficients in additional stream(s)."""
        return self._apply_filter(
            filter_name="afir",
            inputs=[self, *streams],
            named_arguments={
                "dry": dry,
                "wet": wet,
                "length": length,
                "gtype": gtype,
                "irnorm": irnorm,
                "irlink": irlink,
                "irgain": irgain,
                "irfmt": irfmt,
                "maxir": maxir,
                "response": response,
                "channel": channel,
                "size": size,
                "rate": rate,
                "minp": minp,
                "maxp": maxp,
                "nbirs": nbirs,
                "ir": ir,
                "precision": precision,
                "irload": irload,
            },
        )[0]

    def aformat(self) -> "Stream":
        """Convert the input audio to one of the specified formats."""
        return self._apply_filter(
            filter_name="aformat", inputs=[self], named_arguments={}
        )[0]

    def afreqshift(
        self, shift: float = None, level: float = None, order: int = None
    ) -> "Stream":
        """Apply frequency shifting to input audio."""
        return self._apply_filter(
            filter_name="afreqshift",
            inputs=[self],
            named_arguments={
                "shift": shift,
                "level": level,
                "order": order,
            },
        )[0]

    def afwtdn(
        self,
        sigma: float = None,
        levels: int = None,
        wavet: Literal["sym2", "sym4", "rbior68", "deb10", "sym10", "coif5", "bl3"]
        | int = None,
        percent: float = None,
        profile: bool = None,
        adaptive: bool = None,
        samples: int = None,
        softness: float = None,
    ) -> "Stream":
        """Denoise audio stream using Wavelets."""
        return self._apply_filter(
            filter_name="afwtdn",
            inputs=[self],
            named_arguments={
                "sigma": sigma,
                "levels": levels,
                "wavet": wavet,
                "percent": percent,
                "profile": profile,
                "adaptive": adaptive,
                "samples": samples,
                "softness": softness,
            },
        )[0]

    def agate(
        self,
        level_in: float = None,
        mode: Literal["downward", "upward"] | int = None,
        range: float = None,
        threshold: float = None,
        ratio: float = None,
        attack: float = None,
        release: float = None,
        makeup: float = None,
        knee: float = None,
        detection: Literal["peak", "rms"] | int = None,
        link: Literal["average", "maximum"] | int = None,
        level_sc: float = None,
    ) -> "Stream":
        """Audio gate."""
        return self._apply_filter(
            filter_name="agate",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "mode": mode,
                "range": range,
                "threshold": threshold,
                "ratio": ratio,
                "attack": attack,
                "release": release,
                "makeup": makeup,
                "knee": knee,
                "detection": detection,
                "link": link,
                "level_sc": level_sc,
            },
        )[0]

    def agraphmonitor(
        self,
        size: str = None,
        s: str = None,
        opacity: float = None,
        o: float = None,
        mode: Literal["full", "compact", "nozero", "noeof", "nodisabled"] = None,
        m: Literal["full", "compact", "nozero", "noeof", "nodisabled"] = None,
        flags: Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ] = None,
        f: Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ] = None,
        rate: str = None,
        r: str = None,
    ) -> "Stream":
        """Show various filtergraph stats."""
        return self._apply_filter(
            filter_name="agraphmonitor",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "opacity": opacity,
                "o": o,
                "mode": mode,
                "m": m,
                "flags": flags,
                "f": f,
                "rate": rate,
                "r": r,
            },
        )[0]

    def ahistogram(
        self,
        dmode: Literal["single", "separate"] | int = None,
        rate: str = None,
        r: str = None,
        size: str = None,
        s: str = None,
        scale: Literal["log", "sqrt", "cbrt", "lin", "rlog"] | int = None,
        ascale: Literal["log", "lin"] | int = None,
        acount: int = None,
        rheight: float = None,
        slide: Literal["replace", "scroll"] | int = None,
        hmode: Literal["abs", "sign"] | int = None,
    ) -> "Stream":
        """Convert input audio to histogram video output."""
        return self._apply_filter(
            filter_name="ahistogram",
            inputs=[self],
            named_arguments={
                "dmode": dmode,
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "scale": scale,
                "ascale": ascale,
                "acount": acount,
                "rheight": rheight,
                "slide": slide,
                "hmode": hmode,
            },
        )[0]

    def aiir(
        self,
        zeros: str = None,
        z: str = None,
        poles: str = None,
        p: str = None,
        gains: str = None,
        k: str = None,
        dry: float = None,
        wet: float = None,
        format: Literal["ll", "sf", "tf", "zp", "pr", "pd", "sp"] | int = None,
        f: Literal["ll", "sf", "tf", "zp", "pr", "pd", "sp"] | int = None,
        process: Literal["d", "s", "p"] | int = None,
        r: Literal["d", "s", "p"] | int = None,
        precision: Literal["dbl", "flt", "i32", "i16"] | int = None,
        e: Literal["dbl", "flt", "i32", "i16"] | int = None,
        normalize: bool = None,
        n: bool = None,
        mix: float = None,
        response: bool = None,
        channel: int = None,
        size: str = None,
        rate: str = None,
    ) -> "FilterMultiOutput":
        """Apply Infinite Impulse Response filter with supplied coefficients."""
        return self._apply_dynamic_outputs_filter(
            filter_name="aiir",
            inputs=[self],
            named_arguments={
                "zeros": zeros,
                "z": z,
                "poles": poles,
                "p": p,
                "gains": gains,
                "k": k,
                "dry": dry,
                "wet": wet,
                "format": format,
                "f": f,
                "process": process,
                "r": r,
                "precision": precision,
                "e": e,
                "normalize": normalize,
                "n": n,
                "mix": mix,
                "response": response,
                "channel": channel,
                "size": size,
                "rate": rate,
            },
        )

    def aintegral(self) -> "Stream":
        """Compute integral of input audio."""
        return self._apply_filter(
            filter_name="aintegral", inputs=[self], named_arguments={}
        )[0]

    def ainterleave(
        self,
        *streams: "Stream",
        nb_inputs: int = None,
        n: int = None,
        duration: Literal["longest", "shortest", "first"] | int = None,
    ) -> "Stream":
        """Temporally interleave audio inputs."""
        return self._apply_filter(
            filter_name="ainterleave",
            inputs=[self, *streams],
            named_arguments={
                "nb_inputs": nb_inputs,
                "n": n,
                "duration": duration,
            },
        )[0]

    def alatency(self) -> "Stream":
        """Report audio filtering latency."""
        return self._apply_filter(
            filter_name="alatency", inputs=[self], named_arguments={}
        )[0]

    def alimiter(
        self,
        level_in: float = None,
        level_out: float = None,
        limit: float = None,
        attack: float = None,
        release: float = None,
        asc: bool = None,
        asc_level: float = None,
        level: bool = None,
        latency: bool = None,
    ) -> "Stream":
        """Audio lookahead limiter."""
        return self._apply_filter(
            filter_name="alimiter",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "limit": limit,
                "attack": attack,
                "release": release,
                "asc": asc,
                "asc_level": asc_level,
                "level": level,
                "latency": latency,
            },
        )[0]

    def allpass(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        order: int = None,
        o: int = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
    ) -> "Stream":
        """Apply a two-pole all-pass filter."""
        return self._apply_filter(
            filter_name="allpass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "order": order,
                "o": o,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
            },
        )[0]

    def aloop(
        self, loop: int = None, size: str = None, start: str = None, time: str = None
    ) -> "Stream":
        """Loop audio samples."""
        return self._apply_filter(
            filter_name="aloop",
            inputs=[self],
            named_arguments={
                "loop": loop,
                "size": size,
                "start": start,
                "time": time,
            },
        )[0]

    def alphaextract(self) -> "Stream":
        """Extract an alpha channel as a grayscale image component."""
        return self._apply_filter(
            filter_name="alphaextract", inputs=[self], named_arguments={}
        )[0]

    def alphamerge(self, alpha_stream: "Stream") -> "Stream":
        """Copy the luma value of the second input into the alpha channel of the first input."""
        return self._apply_filter(
            filter_name="alphamerge", inputs=[self, alpha_stream], named_arguments={}
        )[0]

    def amerge(self, *streams: "Stream", inputs: int = None) -> "Stream":
        """Merge two or more audio streams into a single multi-channel stream."""
        return self._apply_filter(
            filter_name="amerge",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
            },
        )[0]

    def ametadata(
        self,
        mode: Literal["select", "add", "modify", "delete", "print"] | int = None,
        key: str = None,
        value: str = None,
        function: Literal[
            "same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"
        ]
        | int = None,
        expr: str = None,
        file: str = None,
        direct: bool = None,
    ) -> "Stream":
        """Manipulate audio frame metadata."""
        return self._apply_filter(
            filter_name="ametadata",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "key": key,
                "value": value,
                "function": function,
                "expr": expr,
                "file": file,
                "direct": direct,
            },
        )[0]

    def amix(
        self,
        *streams: "Stream",
        inputs: int = None,
        duration: Literal["longest", "shortest", "first"] | int = None,
        dropout_transition: float = None,
        weights: str = None,
        normalize: bool = None,
    ) -> "Stream":
        """Audio mixing."""
        return self._apply_filter(
            filter_name="amix",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "duration": duration,
                "dropout_transition": dropout_transition,
                "weights": weights,
                "normalize": normalize,
            },
        )[0]

    def amplify(
        self,
        radius: int = None,
        factor: float = None,
        threshold: float = None,
        tolerance: float = None,
        low: float = None,
        high: float = None,
        planes: str = None,
    ) -> "Stream":
        """Amplify changes between successive video frames."""
        return self._apply_filter(
            filter_name="amplify",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "factor": factor,
                "threshold": threshold,
                "tolerance": tolerance,
                "low": low,
                "high": high,
                "planes": planes,
            },
        )[0]

    def amultiply(self, multiply1_stream: "Stream") -> "Stream":
        """Multiply two audio streams."""
        return self._apply_filter(
            filter_name="amultiply", inputs=[self, multiply1_stream], named_arguments={}
        )[0]

    def anequalizer(
        self,
        params: str = None,
        curves: bool = None,
        size: str = None,
        mgain: float = None,
        fscale: Literal["lin", "log"] | int = None,
        colors: str = None,
    ) -> "FilterMultiOutput":
        """Apply high-order audio parametric multi band equalizer."""
        return self._apply_dynamic_outputs_filter(
            filter_name="anequalizer",
            inputs=[self],
            named_arguments={
                "params": params,
                "curves": curves,
                "size": size,
                "mgain": mgain,
                "fscale": fscale,
                "colors": colors,
            },
        )

    def anlmdn(
        self,
        strength: float = None,
        s: float = None,
        patch: str = None,
        p: str = None,
        research: str = None,
        r: str = None,
        output: Literal["i", "o", "n"] | int = None,
        o: Literal["i", "o", "n"] | int = None,
        smooth: float = None,
        m: float = None,
    ) -> "Stream":
        """Reduce broadband noise from stream using Non-Local Means."""
        return self._apply_filter(
            filter_name="anlmdn",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "s": s,
                "patch": patch,
                "p": p,
                "research": research,
                "r": r,
                "output": output,
                "o": o,
                "smooth": smooth,
                "m": m,
            },
        )[0]

    def anlmf(
        self,
        desired_stream: "Stream",
        order: int = None,
        mu: float = None,
        eps: float = None,
        leakage: float = None,
        out_mode: Literal["i", "d", "o", "n", "e"] | int = None,
        precision: Literal["auto", "float", "double"] | int = None,
    ) -> "Stream":
        """Apply Normalized Least-Mean-Fourth algorithm to first audio stream."""
        return self._apply_filter(
            filter_name="anlmf",
            inputs=[self, desired_stream],
            named_arguments={
                "order": order,
                "mu": mu,
                "eps": eps,
                "leakage": leakage,
                "out_mode": out_mode,
                "precision": precision,
            },
        )[0]

    def anlms(
        self,
        desired_stream: "Stream",
        order: int = None,
        mu: float = None,
        eps: float = None,
        leakage: float = None,
        out_mode: Literal["i", "d", "o", "n", "e"] | int = None,
        precision: Literal["auto", "float", "double"] | int = None,
    ) -> "Stream":
        """Apply Normalized Least-Mean-Squares algorithm to first audio stream."""
        return self._apply_filter(
            filter_name="anlms",
            inputs=[self, desired_stream],
            named_arguments={
                "order": order,
                "mu": mu,
                "eps": eps,
                "leakage": leakage,
                "out_mode": out_mode,
                "precision": precision,
            },
        )[0]

    def anull(self) -> "Stream":
        """Pass the source unchanged to the output."""
        return self._apply_filter(
            filter_name="anull", inputs=[self], named_arguments={}
        )[0]

    def apad(
        self,
        packet_size: int = None,
        pad_len: str = None,
        whole_len: str = None,
        pad_dur: str = None,
        whole_dur: str = None,
    ) -> "Stream":
        """Pad audio with silence."""
        return self._apply_filter(
            filter_name="apad",
            inputs=[self],
            named_arguments={
                "packet_size": packet_size,
                "pad_len": pad_len,
                "whole_len": whole_len,
                "pad_dur": pad_dur,
                "whole_dur": whole_dur,
            },
        )[0]

    def aperms(
        self,
        mode: Literal["none", "ro", "rw", "toggle", "random"] | int = None,
        seed: str = None,
    ) -> "Stream":
        """Set permissions for the output audio frame."""
        return self._apply_filter(
            filter_name="aperms",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "seed": seed,
            },
        )[0]

    def aphasemeter(
        self,
        rate: str = None,
        r: str = None,
        size: str = None,
        s: str = None,
        rc: int = None,
        gc: int = None,
        bc: int = None,
        mpc: str = None,
        video: bool = None,
        phasing: bool = None,
        tolerance: float = None,
        t: float = None,
        angle: float = None,
        a: float = None,
        duration: str = None,
        d: str = None,
    ) -> "FilterMultiOutput":
        """Convert input audio to phase meter video output."""
        return self._apply_dynamic_outputs_filter(
            filter_name="aphasemeter",
            inputs=[self],
            named_arguments={
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "rc": rc,
                "gc": gc,
                "bc": bc,
                "mpc": mpc,
                "video": video,
                "phasing": phasing,
                "tolerance": tolerance,
                "t": t,
                "angle": angle,
                "a": a,
                "duration": duration,
                "d": d,
            },
        )

    def aphaser(
        self,
        in_gain: float = None,
        out_gain: float = None,
        delay: float = None,
        decay: float = None,
        speed: float = None,
        type: Literal["triangular", "t", "sinusoidal", "s"] | int = None,
    ) -> "Stream":
        """Add a phasing effect to the audio."""
        return self._apply_filter(
            filter_name="aphaser",
            inputs=[self],
            named_arguments={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delay": delay,
                "decay": decay,
                "speed": speed,
                "type": type,
            },
        )[0]

    def aphaseshift(
        self, shift: float = None, level: float = None, order: int = None
    ) -> "Stream":
        """Apply phase shifting to input audio."""
        return self._apply_filter(
            filter_name="aphaseshift",
            inputs=[self],
            named_arguments={
                "shift": shift,
                "level": level,
                "order": order,
            },
        )[0]

    def apsnr(self, input1_stream: "Stream") -> "Stream":
        """Measure Audio Peak Signal-to-Noise Ratio."""
        return self._apply_filter(
            filter_name="apsnr", inputs=[self, input1_stream], named_arguments={}
        )[0]

    def apsyclip(
        self,
        level_in: float = None,
        level_out: float = None,
        clip: float = None,
        diff: bool = None,
        adaptive: float = None,
        iterations: int = None,
        level: bool = None,
    ) -> "Stream":
        """Audio Psychoacoustic Clipper."""
        return self._apply_filter(
            filter_name="apsyclip",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "clip": clip,
                "diff": diff,
                "adaptive": adaptive,
                "iterations": iterations,
                "level": level,
            },
        )[0]

    def apulsator(
        self,
        level_in: float = None,
        level_out: float = None,
        mode: Literal["sine", "triangle", "square", "sawup", "sawdown"] | int = None,
        amount: float = None,
        offset_l: float = None,
        offset_r: float = None,
        width: float = None,
        timing: Literal["bpm", "ms", "hz"] | int = None,
        bpm: float = None,
        ms: int = None,
        hz: float = None,
    ) -> "Stream":
        """Audio pulsator."""
        return self._apply_filter(
            filter_name="apulsator",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "mode": mode,
                "amount": amount,
                "offset_l": offset_l,
                "offset_r": offset_r,
                "width": width,
                "timing": timing,
                "bpm": bpm,
                "ms": ms,
                "hz": hz,
            },
        )[0]

    def arealtime(self, limit: str = None, speed: float = None) -> "Stream":
        """Slow down filtering to match realtime."""
        return self._apply_filter(
            filter_name="arealtime",
            inputs=[self],
            named_arguments={
                "limit": limit,
                "speed": speed,
            },
        )[0]

    def aresample(self, sample_rate: int = None) -> "Stream":
        """Resample audio data."""
        return self._apply_filter(
            filter_name="aresample",
            inputs=[self],
            named_arguments={
                "sample_rate": sample_rate,
            },
        )[0]

    def areverse(self) -> "Stream":
        """Reverse an audio clip."""
        return self._apply_filter(
            filter_name="areverse", inputs=[self], named_arguments={}
        )[0]

    def arls(
        self,
        desired_stream: "Stream",
        order: int = None,
        lambda_: float = None,
        delta: float = None,
        out_mode: Literal["i", "d", "o", "n", "e"] | int = None,
        precision: Literal["auto", "float", "double"] | int = None,
    ) -> "Stream":
        """Apply Recursive Least Squares algorithm to first audio stream."""
        return self._apply_filter(
            filter_name="arls",
            inputs=[self, desired_stream],
            named_arguments={
                "order": order,
                "lambda": lambda_,
                "delta": delta,
                "out_mode": out_mode,
                "precision": precision,
            },
        )[0]

    def arnndn(self, model: str = None, m: str = None, mix: float = None) -> "Stream":
        """Reduce noise from speech using Recurrent Neural Networks."""
        return self._apply_filter(
            filter_name="arnndn",
            inputs=[self],
            named_arguments={
                "model": model,
                "m": m,
                "mix": mix,
            },
        )[0]

    def asdr(self, input1_stream: "Stream") -> "Stream":
        """Measure Audio Signal-to-Distortion Ratio."""
        return self._apply_filter(
            filter_name="asdr", inputs=[self, input1_stream], named_arguments={}
        )[0]

    def asegment(
        self, timestamps: str = None, samples: str = None
    ) -> "FilterMultiOutput":
        """Segment audio stream."""
        return self._apply_dynamic_outputs_filter(
            filter_name="asegment",
            inputs=[self],
            named_arguments={
                "timestamps": timestamps,
                "samples": samples,
            },
        )

    def aselect(
        self, expr: str = None, e: str = None, outputs: int = None, n: int = None
    ) -> "FilterMultiOutput":
        """Select audio frames to pass in output."""
        return self._apply_dynamic_outputs_filter(
            filter_name="aselect",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "e": e,
                "outputs": outputs,
                "n": n,
            },
        )

    def asendcmd(
        self, commands: str = None, c: str = None, filename: str = None, f: str = None
    ) -> "Stream":
        """Send commands to filters."""
        return self._apply_filter(
            filter_name="asendcmd",
            inputs=[self],
            named_arguments={
                "commands": commands,
                "c": c,
                "filename": filename,
                "f": f,
            },
        )[0]

    def asetnsamples(
        self,
        nb_out_samples: int = None,
        n: int = None,
        pad: bool = None,
        p: bool = None,
    ) -> "Stream":
        """Set the number of samples for each output audio frames."""
        return self._apply_filter(
            filter_name="asetnsamples",
            inputs=[self],
            named_arguments={
                "nb_out_samples": nb_out_samples,
                "n": n,
                "pad": pad,
                "p": p,
            },
        )[0]

    def asetpts(self, expr: str = None) -> "Stream":
        """Set PTS for the output audio frame."""
        return self._apply_filter(
            filter_name="asetpts",
            inputs=[self],
            named_arguments={
                "expr": expr,
            },
        )[0]

    def asetrate(self, sample_rate: int = None, r: int = None) -> "Stream":
        """Change the sample rate without altering the data."""
        return self._apply_filter(
            filter_name="asetrate",
            inputs=[self],
            named_arguments={
                "sample_rate": sample_rate,
                "r": r,
            },
        )[0]

    def asettb(self, expr: str = None, tb: str = None) -> "Stream":
        """Set timebase for the audio output link."""
        return self._apply_filter(
            filter_name="asettb",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "tb": tb,
            },
        )[0]

    def ashowinfo(self) -> "Stream":
        """Show textual information for each audio frame."""
        return self._apply_filter(
            filter_name="ashowinfo", inputs=[self], named_arguments={}
        )[0]

    def asidedata(
        self,
        mode: Literal["select", "delete"] | int = None,
        type: Literal[
            "PANSCAN",
            "A53_CC",
            "STEREO3D",
            "MATRIXENCODING",
            "DOWNMIX_INFO",
            "REPLAYGAIN",
            "DISPLAYMATRIX",
            "AFD",
            "MOTION_VECTORS",
            "SKIP_SAMPLES",
            "AUDIO_SERVICE_TYPE",
            "MASTERING_DISPLAY_METADATA",
            "GOP_TIMECODE",
            "SPHERICAL",
            "CONTENT_LIGHT_LEVEL",
            "ICC_PROFILE",
            "S12M_TIMECOD",
            "DYNAMIC_HDR_PLUS",
            "REGIONS_OF_INTEREST",
            "VIDEO_ENC_PARAMS",
            "SEI_UNREGISTERED",
            "FILM_GRAIN_PARAMS",
            "DETECTION_BOUNDING_BOXES",
            "DETECTION_BBOXES",
            "DOVI_RPU_BUFFER",
            "DOVI_METADATA",
            "DYNAMIC_HDR_VIVID",
            "AMBIENT_VIEWING_ENVIRONMENT",
            "VIDEO_HINT",
        ]
        | int = None,
    ) -> "Stream":
        """Manipulate audio frame side data."""
        return self._apply_filter(
            filter_name="asidedata",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "type": type,
            },
        )[0]

    def asisdr(self, input1_stream: "Stream") -> "Stream":
        """Measure Audio Scale-Invariant Signal-to-Distortion Ratio."""
        return self._apply_filter(
            filter_name="asisdr", inputs=[self, input1_stream], named_arguments={}
        )[0]

    def asoftclip(
        self,
        type: Literal[
            "hard", "tanh", "atan", "cubic", "exp", "alg", "quintic", "sin", "erf"
        ]
        | int = None,
        threshold: float = None,
        output: float = None,
        param: float = None,
        oversample: int = None,
    ) -> "Stream":
        """Audio Soft Clipper."""
        return self._apply_filter(
            filter_name="asoftclip",
            inputs=[self],
            named_arguments={
                "type": type,
                "threshold": threshold,
                "output": output,
                "param": param,
                "oversample": oversample,
            },
        )[0]

    def aspectralstats(
        self,
        win_size: int = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
        overlap: float = None,
        measure: Literal[
            "none",
            "all",
            "mean",
            "variance",
            "centroid",
            "spread",
            "skewness",
            "kurtosis",
            "entropy",
            "flatness",
            "crest",
            "flux",
            "slope",
            "decrease",
            "rolloff",
        ] = None,
    ) -> "Stream":
        """Show frequency domain statistics about audio frames."""
        return self._apply_filter(
            filter_name="aspectralstats",
            inputs=[self],
            named_arguments={
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                "measure": measure,
            },
        )[0]

    def asplit(self, outputs: int = None) -> "FilterMultiOutput":
        """Pass on the audio input to N audio outputs."""
        return self._apply_dynamic_outputs_filter(
            filter_name="asplit",
            inputs=[self],
            named_arguments={
                "outputs": outputs,
            },
        )

    def ass(
        self,
        filename: str = None,
        f: str = None,
        original_size: str = None,
        fontsdir: str = None,
        alpha: bool = None,
        shaping: Literal["auto", "simple", "complex"] | int = None,
    ) -> "Stream":
        """Render ASS subtitles onto input video using the libass library."""
        return self._apply_filter(
            filter_name="ass",
            inputs=[self],
            named_arguments={
                "filename": filename,
                "f": f,
                "original_size": original_size,
                "fontsdir": fontsdir,
                "alpha": alpha,
                "shaping": shaping,
            },
        )[0]

    def astats(
        self,
        length: float = None,
        metadata: bool = None,
        reset: int = None,
        measure_perchannel: Literal[
            "none",
            "all",
            "Bit_depth",
            "Crest_factor",
            "DC_offset",
            "Dynamic_range",
            "Entropy",
            "Flat_factor",
            "Max_difference",
            "Max_level",
            "Mean_difference",
            "Min_difference",
            "Min_level",
            "Noise_floor",
            "Noise_floor_count",
            "Number_of_Infs",
            "Number_of_NaNs",
            "Number_of_denormals",
            "Number_of_samples",
            "Peak_count",
            "Peak_level",
            "RMS_difference",
            "RMS_level",
            "RMS_peak",
            "RMS_trough",
            "Zero_crossings",
            "Zero_crossings_rate",
            "Abs_Peak_count",
        ] = None,
        measure_overall: Literal[
            "none",
            "all",
            "Bit_depth",
            "Crest_factor",
            "DC_offset",
            "Dynamic_range",
            "Entropy",
            "Flat_factor",
            "Max_difference",
            "Max_level",
            "Mean_difference",
            "Min_difference",
            "Min_level",
            "Noise_floor",
            "Noise_floor_count",
            "Number_of_Infs",
            "Number_of_NaNs",
            "Number_of_denormals",
            "Number_of_samples",
            "Peak_count",
            "Peak_level",
            "RMS_difference",
            "RMS_level",
            "RMS_peak",
            "RMS_trough",
            "Zero_crossings",
            "Zero_crossings_rate",
            "Abs_Peak_count",
        ] = None,
    ) -> "Stream":
        """Show time domain statistics about audio frames."""
        return self._apply_filter(
            filter_name="astats",
            inputs=[self],
            named_arguments={
                "length": length,
                "metadata": metadata,
                "reset": reset,
                "measure_perchannel": measure_perchannel,
                "measure_overall": measure_overall,
            },
        )[0]

    def astreamselect(
        self, *streams: "Stream", inputs: int = None, map: str = None
    ) -> "FilterMultiOutput":
        """Select audio streams"""
        return self._apply_dynamic_outputs_filter(
            filter_name="astreamselect",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "map": map,
            },
        )

    def asubboost(
        self,
        dry: float = None,
        wet: float = None,
        boost: float = None,
        decay: float = None,
        feedback: float = None,
        cutoff: float = None,
        slope: float = None,
        delay: float = None,
        channels: str = None,
    ) -> "Stream":
        """Boost subwoofer frequencies."""
        return self._apply_filter(
            filter_name="asubboost",
            inputs=[self],
            named_arguments={
                "dry": dry,
                "wet": wet,
                "boost": boost,
                "decay": decay,
                "feedback": feedback,
                "cutoff": cutoff,
                "slope": slope,
                "delay": delay,
                "channels": channels,
            },
        )[0]

    def asubcut(
        self, cutoff: float = None, order: int = None, level: float = None
    ) -> "Stream":
        """Cut subwoofer frequencies."""
        return self._apply_filter(
            filter_name="asubcut",
            inputs=[self],
            named_arguments={
                "cutoff": cutoff,
                "order": order,
                "level": level,
            },
        )[0]

    def asupercut(
        self, cutoff: float = None, order: int = None, level: float = None
    ) -> "Stream":
        """Cut super frequencies."""
        return self._apply_filter(
            filter_name="asupercut",
            inputs=[self],
            named_arguments={
                "cutoff": cutoff,
                "order": order,
                "level": level,
            },
        )[0]

    def asuperpass(
        self,
        centerf: float = None,
        order: int = None,
        qfactor: float = None,
        level: float = None,
    ) -> "Stream":
        """Apply high order Butterworth band-pass filter."""
        return self._apply_filter(
            filter_name="asuperpass",
            inputs=[self],
            named_arguments={
                "centerf": centerf,
                "order": order,
                "qfactor": qfactor,
                "level": level,
            },
        )[0]

    def asuperstop(
        self,
        centerf: float = None,
        order: int = None,
        qfactor: float = None,
        level: float = None,
    ) -> "Stream":
        """Apply high order Butterworth band-stop filter."""
        return self._apply_filter(
            filter_name="asuperstop",
            inputs=[self],
            named_arguments={
                "centerf": centerf,
                "order": order,
                "qfactor": qfactor,
                "level": level,
            },
        )[0]

    def atadenoise(
        self,
        _0a: float = None,
        _0b: float = None,
        _1a: float = None,
        _1b: float = None,
        _2a: float = None,
        _2b: float = None,
        s: int = None,
        p: str = None,
        a: Literal["p", "s"] | int = None,
        _0s: float = None,
        _1s: float = None,
        _2s: float = None,
    ) -> "Stream":
        """Apply an Adaptive Temporal Averaging Denoiser."""
        return self._apply_filter(
            filter_name="atadenoise",
            inputs=[self],
            named_arguments={
                "0a": _0a,
                "0b": _0b,
                "1a": _1a,
                "1b": _1b,
                "2a": _2a,
                "2b": _2b,
                "s": s,
                "p": p,
                "a": a,
                "0s": _0s,
                "1s": _1s,
                "2s": _2s,
            },
        )[0]

    def atempo(self, tempo: float = None) -> "Stream":
        """Adjust audio tempo."""
        return self._apply_filter(
            filter_name="atempo",
            inputs=[self],
            named_arguments={
                "tempo": tempo,
            },
        )[0]

    def atilt(
        self,
        freq: float = None,
        slope: float = None,
        width: float = None,
        order: int = None,
        level: float = None,
    ) -> "Stream":
        """Apply spectral tilt to audio."""
        return self._apply_filter(
            filter_name="atilt",
            inputs=[self],
            named_arguments={
                "freq": freq,
                "slope": slope,
                "width": width,
                "order": order,
                "level": level,
            },
        )[0]

    def atrim(
        self,
        start: str = None,
        starti: str = None,
        end: str = None,
        endi: str = None,
        start_pts: str = None,
        end_pts: str = None,
        duration: str = None,
        durationi: str = None,
        start_sample: str = None,
        end_sample: str = None,
    ) -> "Stream":
        """Pick one continuous section from the input, drop the rest."""
        return self._apply_filter(
            filter_name="atrim",
            inputs=[self],
            named_arguments={
                "start": start,
                "starti": starti,
                "end": end,
                "endi": endi,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "durationi": durationi,
                "start_sample": start_sample,
                "end_sample": end_sample,
            },
        )[0]

    def avectorscope(
        self,
        mode: Literal["lissajous", "lissajous_xy", "polar"] | int = None,
        m: Literal["lissajous", "lissajous_xy", "polar"] | int = None,
        rate: str = None,
        r: str = None,
        size: str = None,
        s: str = None,
        rc: int = None,
        gc: int = None,
        bc: int = None,
        ac: int = None,
        rf: int = None,
        gf: int = None,
        bf: int = None,
        af: int = None,
        zoom: float = None,
        draw: Literal["dot", "line", "aaline"] | int = None,
        scale: Literal["lin", "sqrt", "cbrt", "log"] | int = None,
        swap: bool = None,
        mirror: Literal["none", "x", "y", "xy"] | int = None,
    ) -> "Stream":
        """Convert input audio to vectorscope video output."""
        return self._apply_filter(
            filter_name="avectorscope",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "m": m,
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "rc": rc,
                "gc": gc,
                "bc": bc,
                "ac": ac,
                "rf": rf,
                "gf": gf,
                "bf": bf,
                "af": af,
                "zoom": zoom,
                "draw": draw,
                "scale": scale,
                "swap": swap,
                "mirror": mirror,
            },
        )[0]

    def avgblur(
        self, sizeX: int = None, planes: int = None, sizeY: int = None
    ) -> "Stream":
        """Apply Average Blur filter."""
        return self._apply_filter(
            filter_name="avgblur",
            inputs=[self],
            named_arguments={
                "sizeX": sizeX,
                "planes": planes,
                "sizeY": sizeY,
            },
        )[0]

    def axcorrelate(
        self,
        axcorrelate1_stream: "Stream",
        size: int = None,
        algo: Literal["slow", "fast", "best"] | int = None,
    ) -> "Stream":
        """Cross-correlate two audio streams."""
        return self._apply_filter(
            filter_name="axcorrelate",
            inputs=[self, axcorrelate1_stream],
            named_arguments={
                "size": size,
                "algo": algo,
            },
        )[0]

    def azmq(self, bind_address: str = None, b: str = None) -> "Stream":
        """Receive commands through ZMQ and broker them to filters."""
        return self._apply_filter(
            filter_name="azmq",
            inputs=[self],
            named_arguments={
                "bind_address": bind_address,
                "b": b,
            },
        )[0]

    def backgroundkey(
        self, threshold: float = None, similarity: float = None, blend: float = None
    ) -> "Stream":
        """Turns a static background into transparency."""
        return self._apply_filter(
            filter_name="backgroundkey",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def bandpass(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        csg: bool = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply a two-pole Butterworth band-pass filter."""
        return self._apply_filter(
            filter_name="bandpass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "csg": csg,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def bandreject(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply a two-pole Butterworth band-reject filter."""
        return self._apply_filter(
            filter_name="bandreject",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def bass(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        gain: float = None,
        g: float = None,
        poles: int = None,
        p: int = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Boost or cut lower frequencies."""
        return self._apply_filter(
            filter_name="bass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def bbox(self, min_val: int = None) -> "Stream":
        """Compute bounding box for each frame."""
        return self._apply_filter(
            filter_name="bbox",
            inputs=[self],
            named_arguments={
                "min_val": min_val,
            },
        )[0]

    def bench(self, action: Literal["start", "stop"] | int = None) -> "Stream":
        """Benchmark part of a filtergraph."""
        return self._apply_filter(
            filter_name="bench",
            inputs=[self],
            named_arguments={
                "action": action,
            },
        )[0]

    def bilateral(
        self, sigmaS: float = None, sigmaR: float = None, planes: int = None
    ) -> "Stream":
        """Apply Bilateral filter."""
        return self._apply_filter(
            filter_name="bilateral",
            inputs=[self],
            named_arguments={
                "sigmaS": sigmaS,
                "sigmaR": sigmaR,
                "planes": planes,
            },
        )[0]

    def biquad(
        self,
        a0: float = None,
        a1: float = None,
        a2: float = None,
        b0: float = None,
        b1: float = None,
        b2: float = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply a biquad IIR filter with the given coefficients."""
        return self._apply_filter(
            filter_name="biquad",
            inputs=[self],
            named_arguments={
                "a0": a0,
                "a1": a1,
                "a2": a2,
                "b0": b0,
                "b1": b1,
                "b2": b2,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def bitplanenoise(self, bitplane: int = None, filter: bool = None) -> "Stream":
        """Measure bit plane noise."""
        return self._apply_filter(
            filter_name="bitplanenoise",
            inputs=[self],
            named_arguments={
                "bitplane": bitplane,
                "filter": filter,
            },
        )[0]

    def blackdetect(
        self,
        d: float = None,
        black_min_duration: float = None,
        picture_black_ratio_th: float = None,
        pic_th: float = None,
        pixel_black_th: float = None,
        pix_th: float = None,
        alpha: bool = None,
    ) -> "Stream":
        """Detect video intervals that are (almost) black."""
        return self._apply_filter(
            filter_name="blackdetect",
            inputs=[self],
            named_arguments={
                "d": d,
                "black_min_duration": black_min_duration,
                "picture_black_ratio_th": picture_black_ratio_th,
                "pic_th": pic_th,
                "pixel_black_th": pixel_black_th,
                "pix_th": pix_th,
                "alpha": alpha,
            },
        )[0]

    def blackframe(
        self, amount: int = None, threshold: int = None, thresh: int = None
    ) -> "Stream":
        """Detect frames that are (almost) black."""
        return self._apply_filter(
            filter_name="blackframe",
            inputs=[self],
            named_arguments={
                "amount": amount,
                "threshold": threshold,
                "thresh": thresh,
            },
        )[0]

    def blend(
        self,
        bottom_stream: "Stream",
        c0_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        c1_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        c2_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        c3_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        all_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        c0_expr: str = None,
        c1_expr: str = None,
        c2_expr: str = None,
        c3_expr: str = None,
        all_expr: str = None,
        c0_opacity: float = None,
        c1_opacity: float = None,
        c2_opacity: float = None,
        c3_opacity: float = None,
        all_opacity: float = None,
    ) -> "Stream":
        """Blend two video frames into each other."""
        return self._apply_filter(
            filter_name="blend",
            inputs=[self, bottom_stream],
            named_arguments={
                "c0_mode": c0_mode,
                "c1_mode": c1_mode,
                "c2_mode": c2_mode,
                "c3_mode": c3_mode,
                "all_mode": all_mode,
                "c0_expr": c0_expr,
                "c1_expr": c1_expr,
                "c2_expr": c2_expr,
                "c3_expr": c3_expr,
                "all_expr": all_expr,
                "c0_opacity": c0_opacity,
                "c1_opacity": c1_opacity,
                "c2_opacity": c2_opacity,
                "c3_opacity": c3_opacity,
                "all_opacity": all_opacity,
            },
        )[0]

    def blockdetect(
        self, period_min: int = None, period_max: int = None, planes: int = None
    ) -> "Stream":
        """Blockdetect filter."""
        return self._apply_filter(
            filter_name="blockdetect",
            inputs=[self],
            named_arguments={
                "period_min": period_min,
                "period_max": period_max,
                "planes": planes,
            },
        )[0]

    def blurdetect(
        self,
        high: float = None,
        low: float = None,
        radius: int = None,
        block_pct: int = None,
        block_width: int = None,
        block_height: int = None,
        planes: int = None,
    ) -> "Stream":
        """Blurdetect filter."""
        return self._apply_filter(
            filter_name="blurdetect",
            inputs=[self],
            named_arguments={
                "high": high,
                "low": low,
                "radius": radius,
                "block_pct": block_pct,
                "block_width": block_width,
                "block_height": block_height,
                "planes": planes,
            },
        )[0]

    def bm3d(
        self,
        *streams: "Stream",
        sigma: float = None,
        block: int = None,
        bstep: int = None,
        group: int = None,
        range: int = None,
        mstep: int = None,
        thmse: float = None,
        hdthr: float = None,
        estim: Literal["basic", "final"] | int = None,
        ref: bool = None,
        planes: int = None,
    ) -> "Stream":
        """Block-Matching 3D denoiser."""
        return self._apply_filter(
            filter_name="bm3d",
            inputs=[self, *streams],
            named_arguments={
                "sigma": sigma,
                "block": block,
                "bstep": bstep,
                "group": group,
                "range": range,
                "mstep": mstep,
                "thmse": thmse,
                "hdthr": hdthr,
                "estim": estim,
                "ref": ref,
                "planes": planes,
            },
        )[0]

    def boxblur(
        self,
        luma_radius: str = None,
        lr: str = None,
        luma_power: int = None,
        lp: int = None,
        chroma_radius: str = None,
        cr: str = None,
        chroma_power: int = None,
        cp: int = None,
        alpha_radius: str = None,
        ar: str = None,
        alpha_power: int = None,
        ap: int = None,
    ) -> "Stream":
        """Blur the input."""
        return self._apply_filter(
            filter_name="boxblur",
            inputs=[self],
            named_arguments={
                "luma_radius": luma_radius,
                "lr": lr,
                "luma_power": luma_power,
                "lp": lp,
                "chroma_radius": chroma_radius,
                "cr": cr,
                "chroma_power": chroma_power,
                "cp": cp,
                "alpha_radius": alpha_radius,
                "ar": ar,
                "alpha_power": alpha_power,
                "ap": ap,
            },
        )[0]

    def bwdif(
        self,
        mode: Literal["send_frame", "send_field"] | int = None,
        parity: Literal["tff", "bff", "auto"] | int = None,
        deint: Literal["all", "interlaced"] | int = None,
    ) -> "Stream":
        """Deinterlace the input image."""
        return self._apply_filter(
            filter_name="bwdif",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "parity": parity,
                "deint": deint,
            },
        )[0]

    def cas(self, strength: float = None, planes: str = None) -> "Stream":
        """Contrast Adaptive Sharpen."""
        return self._apply_filter(
            filter_name="cas",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "planes": planes,
            },
        )[0]

    def ccrepack(self) -> "Stream":
        """Repack CEA-708 closed caption metadata"""
        return self._apply_filter(
            filter_name="ccrepack", inputs=[self], named_arguments={}
        )[0]

    def channelmap(self, map: str = None, channel_layout: str = None) -> "Stream":
        """Remap audio channels."""
        return self._apply_filter(
            filter_name="channelmap",
            inputs=[self],
            named_arguments={
                "map": map,
                "channel_layout": channel_layout,
            },
        )[0]

    def channelsplit(
        self, channel_layout: str = None, channels: str = None
    ) -> "FilterMultiOutput":
        """Split audio into per-channel streams."""
        return self._apply_dynamic_outputs_filter(
            filter_name="channelsplit",
            inputs=[self],
            named_arguments={
                "channel_layout": channel_layout,
                "channels": channels,
            },
        )

    def chorus(
        self,
        in_gain: float = None,
        out_gain: float = None,
        delays: str = None,
        decays: str = None,
        speeds: str = None,
        depths: str = None,
    ) -> "Stream":
        """Add a chorus effect to the audio."""
        return self._apply_filter(
            filter_name="chorus",
            inputs=[self],
            named_arguments={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
                "speeds": speeds,
                "depths": depths,
            },
        )[0]

    def chromahold(
        self,
        color: str = None,
        similarity: float = None,
        blend: float = None,
        yuv: bool = None,
    ) -> "Stream":
        """Turns a certain color range into gray."""
        return self._apply_filter(
            filter_name="chromahold",
            inputs=[self],
            named_arguments={
                "color": color,
                "similarity": similarity,
                "blend": blend,
                "yuv": yuv,
            },
        )[0]

    def chromakey(
        self,
        color: str = None,
        similarity: float = None,
        blend: float = None,
        yuv: bool = None,
    ) -> "Stream":
        """Turns a certain color into transparency. Operates on YUV colors."""
        return self._apply_filter(
            filter_name="chromakey",
            inputs=[self],
            named_arguments={
                "color": color,
                "similarity": similarity,
                "blend": blend,
                "yuv": yuv,
            },
        )[0]

    def chromanr(
        self,
        thres: float = None,
        sizew: int = None,
        sizeh: int = None,
        stepw: int = None,
        steph: int = None,
        threy: float = None,
        threu: float = None,
        threv: float = None,
        distance: Literal["manhattan", "euclidean"] | int = None,
    ) -> "Stream":
        """Reduce chrominance noise."""
        return self._apply_filter(
            filter_name="chromanr",
            inputs=[self],
            named_arguments={
                "thres": thres,
                "sizew": sizew,
                "sizeh": sizeh,
                "stepw": stepw,
                "steph": steph,
                "threy": threy,
                "threu": threu,
                "threv": threv,
                "distance": distance,
            },
        )[0]

    def chromashift(
        self,
        cbh: int = None,
        cbv: int = None,
        crh: int = None,
        crv: int = None,
        edge: Literal["smear", "wrap"] | int = None,
    ) -> "Stream":
        """Shift chroma."""
        return self._apply_filter(
            filter_name="chromashift",
            inputs=[self],
            named_arguments={
                "cbh": cbh,
                "cbv": cbv,
                "crh": crh,
                "crv": crv,
                "edge": edge,
            },
        )[0]

    def ciescope(
        self,
        system: Literal[
            "ntsc",
            "470m",
            "ebu",
            "470bg",
            "smpte",
            "240m",
            "apple",
            "widergb",
            "cie1931",
            "hdtv",
            "rec709",
            "uhdtv",
            "rec2020",
            "dcip3",
        ]
        | int = None,
        cie: Literal["xyy", "ucs", "luv"] | int = None,
        gamuts: Literal[
            "ntsc",
            "470m",
            "ebu",
            "470bg",
            "smpte",
            "240m",
            "apple",
            "widergb",
            "cie1931",
            "hdtv",
            "rec709",
            "uhdtv",
            "rec2020",
            "dcip3",
        ] = None,
        size: int = None,
        s: int = None,
        intensity: float = None,
        i: float = None,
        contrast: float = None,
        corrgamma: bool = None,
        showwhite: bool = None,
        gamma: float = None,
        fill: bool = None,
    ) -> "Stream":
        """Video CIE scope."""
        return self._apply_filter(
            filter_name="ciescope",
            inputs=[self],
            named_arguments={
                "system": system,
                "cie": cie,
                "gamuts": gamuts,
                "size": size,
                "s": s,
                "intensity": intensity,
                "i": i,
                "contrast": contrast,
                "corrgamma": corrgamma,
                "showwhite": showwhite,
                "gamma": gamma,
                "fill": fill,
            },
        )[0]

    def codecview(
        self,
        mv: Literal["pf", "bf", "bb"] = None,
        qp: bool = None,
        mv_type: Literal["fp", "bp"] = None,
        mvt: Literal["fp", "bp"] = None,
        frame_type: Literal["if", "pf", "bf"] = None,
        ft: Literal["if", "pf", "bf"] = None,
        block: bool = None,
    ) -> "Stream":
        """Visualize information about some codecs."""
        return self._apply_filter(
            filter_name="codecview",
            inputs=[self],
            named_arguments={
                "mv": mv,
                "qp": qp,
                "mv_type": mv_type,
                "mvt": mvt,
                "frame_type": frame_type,
                "ft": ft,
                "block": block,
            },
        )[0]

    def colorbalance(
        self,
        rs: float = None,
        gs: float = None,
        bs: float = None,
        rm: float = None,
        gm: float = None,
        bm: float = None,
        rh: float = None,
        gh: float = None,
        bh: float = None,
        pl: bool = None,
    ) -> "Stream":
        """Adjust the color balance."""
        return self._apply_filter(
            filter_name="colorbalance",
            inputs=[self],
            named_arguments={
                "rs": rs,
                "gs": gs,
                "bs": bs,
                "rm": rm,
                "gm": gm,
                "bm": bm,
                "rh": rh,
                "gh": gh,
                "bh": bh,
                "pl": pl,
            },
        )[0]

    def colorchannelmixer(
        self,
        rr: float = None,
        rg: float = None,
        rb: float = None,
        ra: float = None,
        gr: float = None,
        gg: float = None,
        gb: float = None,
        ga: float = None,
        br: float = None,
        bg: float = None,
        bb: float = None,
        ba: float = None,
        ar: float = None,
        ag: float = None,
        ab: float = None,
        aa: float = None,
        pc: Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"] | int = None,
        pa: float = None,
    ) -> "Stream":
        """Adjust colors by mixing color channels."""
        return self._apply_filter(
            filter_name="colorchannelmixer",
            inputs=[self],
            named_arguments={
                "rr": rr,
                "rg": rg,
                "rb": rb,
                "ra": ra,
                "gr": gr,
                "gg": gg,
                "gb": gb,
                "ga": ga,
                "br": br,
                "bg": bg,
                "bb": bb,
                "ba": ba,
                "ar": ar,
                "ag": ag,
                "ab": ab,
                "aa": aa,
                "pc": pc,
                "pa": pa,
            },
        )[0]

    def colorcontrast(
        self,
        rc: float = None,
        gm: float = None,
        by: float = None,
        rcw: float = None,
        gmw: float = None,
        byw: float = None,
        pl: float = None,
    ) -> "Stream":
        """Adjust color contrast between RGB components."""
        return self._apply_filter(
            filter_name="colorcontrast",
            inputs=[self],
            named_arguments={
                "rc": rc,
                "gm": gm,
                "by": by,
                "rcw": rcw,
                "gmw": gmw,
                "byw": byw,
                "pl": pl,
            },
        )[0]

    def colorcorrect(
        self,
        rl: float = None,
        bl: float = None,
        rh: float = None,
        bh: float = None,
        saturation: float = None,
        analyze: Literal["manual", "average", "minmax", "median"] | int = None,
    ) -> "Stream":
        """Adjust color white balance selectively for blacks and whites."""
        return self._apply_filter(
            filter_name="colorcorrect",
            inputs=[self],
            named_arguments={
                "rl": rl,
                "bl": bl,
                "rh": rh,
                "bh": bh,
                "saturation": saturation,
                "analyze": analyze,
            },
        )[0]

    def colordetect(
        self, mode: Literal["color_range", "alpha_mode", "all"] = None
    ) -> "Stream":
        """Detect video color properties."""
        return self._apply_filter(
            filter_name="colordetect",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def colorhold(
        self, color: str = None, similarity: float = None, blend: float = None
    ) -> "Stream":
        """Turns a certain color range into gray. Operates on RGB colors."""
        return self._apply_filter(
            filter_name="colorhold",
            inputs=[self],
            named_arguments={
                "color": color,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def colorize(
        self,
        hue: float = None,
        saturation: float = None,
        lightness: float = None,
        mix: float = None,
    ) -> "Stream":
        """Overlay a solid color on the video stream."""
        return self._apply_filter(
            filter_name="colorize",
            inputs=[self],
            named_arguments={
                "hue": hue,
                "saturation": saturation,
                "lightness": lightness,
                "mix": mix,
            },
        )[0]

    def colorkey(
        self, color: str = None, similarity: float = None, blend: float = None
    ) -> "Stream":
        """Turns a certain color into transparency. Operates on RGB colors."""
        return self._apply_filter(
            filter_name="colorkey",
            inputs=[self],
            named_arguments={
                "color": color,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def colorlevels(
        self,
        rimin: float = None,
        gimin: float = None,
        bimin: float = None,
        aimin: float = None,
        rimax: float = None,
        gimax: float = None,
        bimax: float = None,
        aimax: float = None,
        romin: float = None,
        gomin: float = None,
        bomin: float = None,
        aomin: float = None,
        romax: float = None,
        gomax: float = None,
        bomax: float = None,
        aomax: float = None,
        preserve: Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"]
        | int = None,
    ) -> "Stream":
        """Adjust the color levels."""
        return self._apply_filter(
            filter_name="colorlevels",
            inputs=[self],
            named_arguments={
                "rimin": rimin,
                "gimin": gimin,
                "bimin": bimin,
                "aimin": aimin,
                "rimax": rimax,
                "gimax": gimax,
                "bimax": bimax,
                "aimax": aimax,
                "romin": romin,
                "gomin": gomin,
                "bomin": bomin,
                "aomin": aomin,
                "romax": romax,
                "gomax": gomax,
                "bomax": bomax,
                "aomax": aomax,
                "preserve": preserve,
            },
        )[0]

    def colormap(
        self,
        source_stream: "Stream",
        target_stream: "Stream",
        patch_size: str = None,
        nb_patches: int = None,
        type: Literal["relative", "absolute"] | int = None,
        kernel: Literal["euclidean", "weuclidean"] | int = None,
    ) -> "Stream":
        """Apply custom Color Maps to video stream."""
        return self._apply_filter(
            filter_name="colormap",
            inputs=[self, source_stream, target_stream],
            named_arguments={
                "patch_size": patch_size,
                "nb_patches": nb_patches,
                "type": type,
                "kernel": kernel,
            },
        )[0]

    def colormatrix(
        self,
        src: Literal[
            "bt709",
            "fcc",
            "bt601",
            "bt470",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | int = None,
        dst: Literal[
            "bt709",
            "fcc",
            "bt601",
            "bt470",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | int = None,
    ) -> "Stream":
        """Convert color matrix."""
        return self._apply_filter(
            filter_name="colormatrix",
            inputs=[self],
            named_arguments={
                "src": src,
                "dst": dst,
            },
        )[0]

    def colorspace(
        self,
        all: Literal[
            "bt470m",
            "bt470bg",
            "bt601-6-525",
            "bt601-6-625",
            "bt709",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | int = None,
        space: Literal[
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "gbr",
            "bt2020nc",
            "bt2020ncl",
        ]
        | int = None,
        range: Literal["tv", "mpeg", "pc", "jpeg"] | int = None,
        primaries: Literal[
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "smpte428",
            "film",
            "smpte431",
            "smpte432",
            "bt2020",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        trc: Literal[
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "srgb",
            "iec61966-2-1",
            "xvycc",
            "iec61966-2-4",
            "bt2020-10",
            "bt2020-12",
        ]
        | int = None,
        format: Literal[
            "yuv420p",
            "yuv420p10",
            "yuv420p12",
            "yuv422p",
            "yuv422p10",
            "yuv422p12",
            "yuv444p",
            "yuv444p10",
            "yuv444p12",
        ]
        | int = None,
        fast: bool = None,
        dither: Literal["none", "fsb"] | int = None,
        wpadapt: Literal["bradford", "vonkries", "identity"] | int = None,
        iall: Literal[
            "bt470m",
            "bt470bg",
            "bt601-6-525",
            "bt601-6-625",
            "bt709",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | int = None,
        ispace: Literal[
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "gbr",
            "bt2020nc",
            "bt2020ncl",
        ]
        | int = None,
        irange: Literal["tv", "mpeg", "pc", "jpeg"] | int = None,
        iprimaries: Literal[
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "smpte428",
            "film",
            "smpte431",
            "smpte432",
            "bt2020",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        itrc: Literal[
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "srgb",
            "iec61966-2-1",
            "xvycc",
            "iec61966-2-4",
            "bt2020-10",
            "bt2020-12",
        ]
        | int = None,
    ) -> "Stream":
        """Convert between colorspaces."""
        return self._apply_filter(
            filter_name="colorspace",
            inputs=[self],
            named_arguments={
                "all": all,
                "space": space,
                "range": range,
                "primaries": primaries,
                "trc": trc,
                "format": format,
                "fast": fast,
                "dither": dither,
                "wpadapt": wpadapt,
                "iall": iall,
                "ispace": ispace,
                "irange": irange,
                "iprimaries": iprimaries,
                "itrc": itrc,
            },
        )[0]

    def colortemperature(
        self, temperature: float = None, mix: float = None, pl: float = None
    ) -> "Stream":
        """Adjust color temperature of video."""
        return self._apply_filter(
            filter_name="colortemperature",
            inputs=[self],
            named_arguments={
                "temperature": temperature,
                "mix": mix,
                "pl": pl,
            },
        )[0]

    def compand(
        self,
        attacks: str = None,
        decays: str = None,
        points: str = None,
        soft_knee: float = None,
        gain: float = None,
        volume: float = None,
        delay: float = None,
    ) -> "Stream":
        """Compress or expand audio dynamic range."""
        return self._apply_filter(
            filter_name="compand",
            inputs=[self],
            named_arguments={
                "attacks": attacks,
                "decays": decays,
                "points": points,
                "soft-knee": soft_knee,
                "gain": gain,
                "volume": volume,
                "delay": delay,
            },
        )[0]

    def compensationdelay(
        self,
        mm: int = None,
        cm: int = None,
        m: int = None,
        dry: float = None,
        wet: float = None,
        temp: int = None,
    ) -> "Stream":
        """Audio Compensation Delay Line."""
        return self._apply_filter(
            filter_name="compensationdelay",
            inputs=[self],
            named_arguments={
                "mm": mm,
                "cm": cm,
                "m": m,
                "dry": dry,
                "wet": wet,
                "temp": temp,
            },
        )[0]

    def concat(
        self,
        *streams: "Stream",
        n: int = None,
        v: int = None,
        a: int = None,
        unsafe: bool = None,
    ) -> "FilterMultiOutput":
        """Concatenate audio and video streams."""
        return self._apply_dynamic_outputs_filter(
            filter_name="concat",
            inputs=[self, *streams],
            named_arguments={
                "n": n,
                "v": v,
                "a": a,
                "unsafe": unsafe,
            },
        )

    def convolution(
        self,
        _0m: str = None,
        _1m: str = None,
        _2m: str = None,
        _3m: str = None,
        _0rdiv: float = None,
        _1rdiv: float = None,
        _2rdiv: float = None,
        _3rdiv: float = None,
        _0bias: float = None,
        _1bias: float = None,
        _2bias: float = None,
        _3bias: float = None,
        _0mode: Literal["square", "row", "column"] | int = None,
        _1mode: Literal["square", "row", "column"] | int = None,
        _2mode: Literal["square", "row", "column"] | int = None,
        _3mode: Literal["square", "row", "column"] | int = None,
    ) -> "Stream":
        """Apply convolution filter."""
        return self._apply_filter(
            filter_name="convolution",
            inputs=[self],
            named_arguments={
                "0m": _0m,
                "1m": _1m,
                "2m": _2m,
                "3m": _3m,
                "0rdiv": _0rdiv,
                "1rdiv": _1rdiv,
                "2rdiv": _2rdiv,
                "3rdiv": _3rdiv,
                "0bias": _0bias,
                "1bias": _1bias,
                "2bias": _2bias,
                "3bias": _3bias,
                "0mode": _0mode,
                "1mode": _1mode,
                "2mode": _2mode,
                "3mode": _3mode,
            },
        )[0]

    def convolve(
        self,
        impulse_stream: "Stream",
        planes: int = None,
        impulse: Literal["first", "all"] | int = None,
        noise: float = None,
    ) -> "Stream":
        """Convolve first video stream with second video stream."""
        return self._apply_filter(
            filter_name="convolve",
            inputs=[self, impulse_stream],
            named_arguments={
                "planes": planes,
                "impulse": impulse,
                "noise": noise,
            },
        )[0]

    def copy(self) -> "Stream":
        """Copy the input video unchanged to the output."""
        return self._apply_filter(
            filter_name="copy", inputs=[self], named_arguments={}
        )[0]

    def coreimage(
        self,
        list_filters: bool = None,
        list_generators: bool = None,
        filter: str = None,
        output_rect: str = None,
    ) -> "Stream":
        """Video filtering using CoreImage API."""
        return self._apply_filter(
            filter_name="coreimage",
            inputs=[self],
            named_arguments={
                "list_filters": list_filters,
                "list_generators": list_generators,
                "filter": filter,
                "output_rect": output_rect,
            },
        )[0]

    def corr(self, reference_stream: "Stream") -> "Stream":
        """Calculate the correlation between two video streams."""
        return self._apply_filter(
            filter_name="corr", inputs=[self, reference_stream], named_arguments={}
        )[0]

    def cover_rect(
        self, cover: str = None, mode: Literal["cover", "blur"] | int = None
    ) -> "Stream":
        """Find and cover a user specified object."""
        return self._apply_filter(
            filter_name="cover_rect",
            inputs=[self],
            named_arguments={
                "cover": cover,
                "mode": mode,
            },
        )[0]

    def crop(
        self,
        out_w: str = None,
        w: str = None,
        out_h: str = None,
        h: str = None,
        x: str = None,
        y: str = None,
        keep_aspect: bool = None,
        exact: bool = None,
    ) -> "Stream":
        """Crop the input video."""
        return self._apply_filter(
            filter_name="crop",
            inputs=[self],
            named_arguments={
                "out_w": out_w,
                "w": w,
                "out_h": out_h,
                "h": h,
                "x": x,
                "y": y,
                "keep_aspect": keep_aspect,
                "exact": exact,
            },
        )[0]

    def cropdetect(
        self,
        limit: float = None,
        round: int = None,
        reset: int = None,
        skip: int = None,
        reset_count: int = None,
        max_outliers: int = None,
        mode: Literal["black", "mvedges"] | int = None,
        high: float = None,
        low: float = None,
        mv_threshold: int = None,
    ) -> "Stream":
        """Auto-detect crop size."""
        return self._apply_filter(
            filter_name="cropdetect",
            inputs=[self],
            named_arguments={
                "limit": limit,
                "round": round,
                "reset": reset,
                "skip": skip,
                "reset_count": reset_count,
                "max_outliers": max_outliers,
                "mode": mode,
                "high": high,
                "low": low,
                "mv_threshold": mv_threshold,
            },
        )[0]

    def crossfeed(
        self,
        strength: float = None,
        range: float = None,
        slope: float = None,
        level_in: float = None,
        level_out: float = None,
        block_size: int = None,
    ) -> "Stream":
        """Apply headphone crossfeed filter."""
        return self._apply_filter(
            filter_name="crossfeed",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "range": range,
                "slope": slope,
                "level_in": level_in,
                "level_out": level_out,
                "block_size": block_size,
            },
        )[0]

    def crystalizer(self, i: float = None, c: bool = None) -> "Stream":
        """Simple audio noise sharpening filter."""
        return self._apply_filter(
            filter_name="crystalizer",
            inputs=[self],
            named_arguments={
                "i": i,
                "c": c,
            },
        )[0]

    def cue(self, cue: str = None, preroll: str = None, buffer: str = None) -> "Stream":
        """Delay filtering to match a cue."""
        return self._apply_filter(
            filter_name="cue",
            inputs=[self],
            named_arguments={
                "cue": cue,
                "preroll": preroll,
                "buffer": buffer,
            },
        )[0]

    def curves(
        self,
        preset: Literal[
            "none",
            "color_negative",
            "cross_process",
            "darker",
            "increase_contrast",
            "lighter",
            "linear_contrast",
            "medium_contrast",
            "negative",
            "strong_contrast",
            "vintage",
        ]
        | int = None,
        master: str = None,
        m: str = None,
        red: str = None,
        r: str = None,
        green: str = None,
        g: str = None,
        blue: str = None,
        b: str = None,
        all: str = None,
        psfile: str = None,
        plot: str = None,
        interp: Literal["natural", "pchip"] | int = None,
    ) -> "Stream":
        """Adjust components curves."""
        return self._apply_filter(
            filter_name="curves",
            inputs=[self],
            named_arguments={
                "preset": preset,
                "master": master,
                "m": m,
                "red": red,
                "r": r,
                "green": green,
                "g": g,
                "blue": blue,
                "b": b,
                "all": all,
                "psfile": psfile,
                "plot": plot,
                "interp": interp,
            },
        )[0]

    def datascope(
        self,
        size: str = None,
        s: str = None,
        x: int = None,
        y: int = None,
        mode: Literal["mono", "color", "color2"] | int = None,
        axis: bool = None,
        opacity: float = None,
        format: Literal["hex", "dec"] | int = None,
        components: int = None,
    ) -> "Stream":
        """Video data analysis."""
        return self._apply_filter(
            filter_name="datascope",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "x": x,
                "y": y,
                "mode": mode,
                "axis": axis,
                "opacity": opacity,
                "format": format,
                "components": components,
            },
        )[0]

    def dblur(
        self, angle: float = None, radius: float = None, planes: int = None
    ) -> "Stream":
        """Apply Directional Blur filter."""
        return self._apply_filter(
            filter_name="dblur",
            inputs=[self],
            named_arguments={
                "angle": angle,
                "radius": radius,
                "planes": planes,
            },
        )[0]

    def dcshift(self, shift: float = None, limitergain: float = None) -> "Stream":
        """Apply a DC shift to the audio."""
        return self._apply_filter(
            filter_name="dcshift",
            inputs=[self],
            named_arguments={
                "shift": shift,
                "limitergain": limitergain,
            },
        )[0]

    def dctdnoiz(
        self,
        sigma: float = None,
        s: float = None,
        overlap: int = None,
        expr: str = None,
        e: str = None,
        n: int = None,
    ) -> "Stream":
        """Denoise frames using 2D DCT."""
        return self._apply_filter(
            filter_name="dctdnoiz",
            inputs=[self],
            named_arguments={
                "sigma": sigma,
                "s": s,
                "overlap": overlap,
                "expr": expr,
                "e": e,
                "n": n,
            },
        )[0]

    def deband(
        self,
        _1thr: float = None,
        _2thr: float = None,
        _3thr: float = None,
        _4thr: float = None,
        range: int = None,
        r: int = None,
        direction: float = None,
        d: float = None,
        blur: bool = None,
        b: bool = None,
        coupling: bool = None,
        c: bool = None,
    ) -> "Stream":
        """Debands video."""
        return self._apply_filter(
            filter_name="deband",
            inputs=[self],
            named_arguments={
                "1thr": _1thr,
                "2thr": _2thr,
                "3thr": _3thr,
                "4thr": _4thr,
                "range": range,
                "r": r,
                "direction": direction,
                "d": d,
                "blur": blur,
                "b": b,
                "coupling": coupling,
                "c": c,
            },
        )[0]

    def deblock(
        self,
        filter: Literal["weak", "strong"] | int = None,
        block: int = None,
        alpha: float = None,
        beta: float = None,
        gamma: float = None,
        delta: float = None,
        planes: int = None,
    ) -> "Stream":
        """Deblock video."""
        return self._apply_filter(
            filter_name="deblock",
            inputs=[self],
            named_arguments={
                "filter": filter,
                "block": block,
                "alpha": alpha,
                "beta": beta,
                "gamma": gamma,
                "delta": delta,
                "planes": planes,
            },
        )[0]

    def decimate(
        self,
        *streams: "Stream",
        cycle: int = None,
        dupthresh: float = None,
        scthresh: float = None,
        blockx: int = None,
        blocky: int = None,
        ppsrc: bool = None,
        chroma: bool = None,
        mixed: bool = None,
    ) -> "Stream":
        """Decimate frames (post field matching filter)."""
        return self._apply_filter(
            filter_name="decimate",
            inputs=[self, *streams],
            named_arguments={
                "cycle": cycle,
                "dupthresh": dupthresh,
                "scthresh": scthresh,
                "blockx": blockx,
                "blocky": blocky,
                "ppsrc": ppsrc,
                "chroma": chroma,
                "mixed": mixed,
            },
        )[0]

    def deconvolve(
        self,
        impulse_stream: "Stream",
        planes: int = None,
        impulse: Literal["first", "all"] | int = None,
        noise: float = None,
    ) -> "Stream":
        """Deconvolve first video stream with second video stream."""
        return self._apply_filter(
            filter_name="deconvolve",
            inputs=[self, impulse_stream],
            named_arguments={
                "planes": planes,
                "impulse": impulse,
                "noise": noise,
            },
        )[0]

    def dedot(
        self,
        m: Literal["dotcrawl", "rainbows"] = None,
        lt: float = None,
        tl: float = None,
        tc: float = None,
        ct: float = None,
    ) -> "Stream":
        """Reduce cross-luminance and cross-color."""
        return self._apply_filter(
            filter_name="dedot",
            inputs=[self],
            named_arguments={
                "m": m,
                "lt": lt,
                "tl": tl,
                "tc": tc,
                "ct": ct,
            },
        )[0]

    def deesser(
        self,
        i: float = None,
        m: float = None,
        f: float = None,
        s: Literal["i", "o", "e"] | int = None,
    ) -> "Stream":
        """Apply de-essing to the audio."""
        return self._apply_filter(
            filter_name="deesser",
            inputs=[self],
            named_arguments={
                "i": i,
                "m": m,
                "f": f,
                "s": s,
            },
        )[0]

    def deflate(
        self,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
    ) -> "Stream":
        """Apply deflate effect."""
        return self._apply_filter(
            filter_name="deflate",
            inputs=[self],
            named_arguments={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            },
        )[0]

    def deflicker(
        self,
        size: int = None,
        s: int = None,
        mode: Literal["am", "gm", "hm", "qm", "cm", "pm", "median"] | int = None,
        m: Literal["am", "gm", "hm", "qm", "cm", "pm", "median"] | int = None,
        bypass: bool = None,
    ) -> "Stream":
        """Remove temporal frame luminance variations."""
        return self._apply_filter(
            filter_name="deflicker",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "mode": mode,
                "m": m,
                "bypass": bypass,
            },
        )[0]

    def dejudder(self, cycle: int = None) -> "Stream":
        """Remove judder produced by pullup."""
        return self._apply_filter(
            filter_name="dejudder",
            inputs=[self],
            named_arguments={
                "cycle": cycle,
            },
        )[0]

    def delogo(
        self,
        x: str = None,
        y: str = None,
        w: str = None,
        h: str = None,
        show: bool = None,
    ) -> "Stream":
        """Remove logo from input video."""
        return self._apply_filter(
            filter_name="delogo",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "show": show,
            },
        )[0]

    def deshake(
        self,
        x: int = None,
        y: int = None,
        w: int = None,
        h: int = None,
        rx: int = None,
        ry: int = None,
        edge: Literal["blank", "original", "clamp", "mirror"] | int = None,
        blocksize: int = None,
        contrast: int = None,
        search: Literal["exhaustive", "less"] | int = None,
        filename: str = None,
        opencl: bool = None,
    ) -> "Stream":
        """Stabilize shaky video."""
        return self._apply_filter(
            filter_name="deshake",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "rx": rx,
                "ry": ry,
                "edge": edge,
                "blocksize": blocksize,
                "contrast": contrast,
                "search": search,
                "filename": filename,
                "opencl": opencl,
            },
        )[0]

    def despill(
        self,
        type: Literal["green", "blue"] | int = None,
        mix: float = None,
        expand: float = None,
        red: float = None,
        green: float = None,
        blue: float = None,
        brightness: float = None,
        alpha: bool = None,
    ) -> "Stream":
        """Despill video."""
        return self._apply_filter(
            filter_name="despill",
            inputs=[self],
            named_arguments={
                "type": type,
                "mix": mix,
                "expand": expand,
                "red": red,
                "green": green,
                "blue": blue,
                "brightness": brightness,
                "alpha": alpha,
            },
        )[0]

    def detelecine(
        self,
        first_field: Literal["top", "t", "bottom", "b"] | int = None,
        pattern: str = None,
        start_frame: int = None,
    ) -> "Stream":
        """Apply an inverse telecine pattern."""
        return self._apply_filter(
            filter_name="detelecine",
            inputs=[self],
            named_arguments={
                "first_field": first_field,
                "pattern": pattern,
                "start_frame": start_frame,
            },
        )[0]

    def dialoguenhance(
        self, original: float = None, enhance: float = None, voice: float = None
    ) -> "Stream":
        """Audio Dialogue Enhancement."""
        return self._apply_filter(
            filter_name="dialoguenhance",
            inputs=[self],
            named_arguments={
                "original": original,
                "enhance": enhance,
                "voice": voice,
            },
        )[0]

    def dilation(
        self,
        coordinates: int = None,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
    ) -> "Stream":
        """Apply dilation effect."""
        return self._apply_filter(
            filter_name="dilation",
            inputs=[self],
            named_arguments={
                "coordinates": coordinates,
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            },
        )[0]

    def displace(
        self,
        xmap_stream: "Stream",
        ymap_stream: "Stream",
        edge: Literal["blank", "smear", "wrap", "mirror"] | int = None,
    ) -> "Stream":
        """Displace pixels."""
        return self._apply_filter(
            filter_name="displace",
            inputs=[self, xmap_stream, ymap_stream],
            named_arguments={
                "edge": edge,
            },
        )[0]

    def doubleweave(
        self, first_field: Literal["top", "t", "bottom", "b"] | int = None
    ) -> "Stream":
        """Weave input video fields into double number of frames."""
        return self._apply_filter(
            filter_name="doubleweave",
            inputs=[self],
            named_arguments={
                "first_field": first_field,
            },
        )[0]

    def drawbox(
        self,
        x: str = None,
        y: str = None,
        width: str = None,
        w: str = None,
        height: str = None,
        h: str = None,
        color: str = None,
        c: str = None,
        thickness: str = None,
        t: str = None,
        replace: bool = None,
        box_source: str = None,
    ) -> "Stream":
        """Draw a colored box on the input video."""
        return self._apply_filter(
            filter_name="drawbox",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "color": color,
                "c": c,
                "thickness": thickness,
                "t": t,
                "replace": replace,
                "box_source": box_source,
            },
        )[0]

    def drawgraph(
        self,
        m1: str = None,
        fg1: str = None,
        m2: str = None,
        fg2: str = None,
        m3: str = None,
        fg3: str = None,
        m4: str = None,
        fg4: str = None,
        bg: str = None,
        min: float = None,
        max: float = None,
        mode: Literal["bar", "dot", "line"] | int = None,
        slide: Literal["frame", "replace", "scroll", "rscroll", "picture"] | int = None,
        size: str = None,
        s: str = None,
        rate: str = None,
        r: str = None,
    ) -> "Stream":
        """Draw a graph using input video metadata."""
        return self._apply_filter(
            filter_name="drawgraph",
            inputs=[self],
            named_arguments={
                "m1": m1,
                "fg1": fg1,
                "m2": m2,
                "fg2": fg2,
                "m3": m3,
                "fg3": fg3,
                "m4": m4,
                "fg4": fg4,
                "bg": bg,
                "min": min,
                "max": max,
                "mode": mode,
                "slide": slide,
                "size": size,
                "s": s,
                "rate": rate,
                "r": r,
            },
        )[0]

    def drawgrid(
        self,
        x: str = None,
        y: str = None,
        width: str = None,
        w: str = None,
        height: str = None,
        h: str = None,
        color: str = None,
        c: str = None,
        thickness: str = None,
        t: str = None,
        replace: bool = None,
    ) -> "Stream":
        """Draw a colored grid on the input video."""
        return self._apply_filter(
            filter_name="drawgrid",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "color": color,
                "c": c,
                "thickness": thickness,
                "t": t,
                "replace": replace,
            },
        )[0]

    def drawtext(
        self,
        fontfile: str = None,
        text: str = None,
        textfile: str = None,
        fontcolor: str = None,
        fontcolor_expr: str = None,
        boxcolor: str = None,
        bordercolor: str = None,
        shadowcolor: str = None,
        box: bool = None,
        boxborderw: str = None,
        line_spacing: int = None,
        fontsize: str = None,
        text_align: Literal[
            "left",
            "L",
            "right",
            "R",
            "center",
            "C",
            "top",
            "T",
            "bottom",
            "B",
            "middle",
            "M",
        ] = None,
        x: str = None,
        y: str = None,
        boxw: int = None,
        boxh: int = None,
        shadowx: int = None,
        shadowy: int = None,
        borderw: int = None,
        tabsize: int = None,
        basetime: str = None,
        font: str = None,
        expansion: Literal["none", "normal", "strftime"] | int = None,
        y_align: Literal["text", "baseline", "font"] | int = None,
        timecode: str = None,
        tc24hmax: bool = None,
        timecode_rate: str = None,
        r: str = None,
        rate: str = None,
        reload: int = None,
        alpha: str = None,
        fix_bounds: bool = None,
        start_number: int = None,
        text_source: str = None,
        ft_load_flags: Literal[
            "default",
            "no_scale",
            "no_hinting",
            "render",
            "no_bitmap",
            "vertical_layout",
            "force_autohint",
            "crop_bitmap",
            "pedantic",
            "ignore_global_advance_width",
            "no_recurse",
            "ignore_transform",
            "monochrome",
            "linear_design",
            "no_autohint",
        ] = None,
    ) -> "Stream":
        """Draw text on top of video frames using libfreetype library."""
        return self._apply_filter(
            filter_name="drawtext",
            inputs=[self],
            named_arguments={
                "fontfile": fontfile,
                "text": text,
                "textfile": textfile,
                "fontcolor": fontcolor,
                "fontcolor_expr": fontcolor_expr,
                "boxcolor": boxcolor,
                "bordercolor": bordercolor,
                "shadowcolor": shadowcolor,
                "box": box,
                "boxborderw": boxborderw,
                "line_spacing": line_spacing,
                "fontsize": fontsize,
                "text_align": text_align,
                "x": x,
                "y": y,
                "boxw": boxw,
                "boxh": boxh,
                "shadowx": shadowx,
                "shadowy": shadowy,
                "borderw": borderw,
                "tabsize": tabsize,
                "basetime": basetime,
                "font": font,
                "expansion": expansion,
                "y_align": y_align,
                "timecode": timecode,
                "tc24hmax": tc24hmax,
                "timecode_rate": timecode_rate,
                "r": r,
                "rate": rate,
                "reload": reload,
                "alpha": alpha,
                "fix_bounds": fix_bounds,
                "start_number": start_number,
                "text_source": text_source,
                "ft_load_flags": ft_load_flags,
            },
        )[0]

    def drmeter(self, length: float = None) -> "Stream":
        """Measure audio dynamic range."""
        return self._apply_filter(
            filter_name="drmeter",
            inputs=[self],
            named_arguments={
                "length": length,
            },
        )[0]

    def dynaudnorm(
        self,
        framelen: int = None,
        f: int = None,
        gausssize: int = None,
        g: int = None,
        peak: float = None,
        p: float = None,
        maxgain: float = None,
        m: float = None,
        targetrms: float = None,
        r: float = None,
        coupling: bool = None,
        n: bool = None,
        correctdc: bool = None,
        c: bool = None,
        altboundary: bool = None,
        b: bool = None,
        compress: float = None,
        s: float = None,
        threshold: float = None,
        t: float = None,
        channels: str = None,
        h: str = None,
        overlap: float = None,
        o: float = None,
        curve: str = None,
        v: str = None,
    ) -> "Stream":
        """Dynamic Audio Normalizer."""
        return self._apply_filter(
            filter_name="dynaudnorm",
            inputs=[self],
            named_arguments={
                "framelen": framelen,
                "f": f,
                "gausssize": gausssize,
                "g": g,
                "peak": peak,
                "p": p,
                "maxgain": maxgain,
                "m": m,
                "targetrms": targetrms,
                "r": r,
                "coupling": coupling,
                "n": n,
                "correctdc": correctdc,
                "c": c,
                "altboundary": altboundary,
                "b": b,
                "compress": compress,
                "s": s,
                "threshold": threshold,
                "t": t,
                "channels": channels,
                "h": h,
                "overlap": overlap,
                "o": o,
                "curve": curve,
                "v": v,
            },
        )[0]

    def earwax(self) -> "Stream":
        """Widen the stereo image."""
        return self._apply_filter(
            filter_name="earwax", inputs=[self], named_arguments={}
        )[0]

    def ebur128(
        self,
        video: bool = None,
        size: str = None,
        meter: int = None,
        framelog: Literal["quiet", "info", "verbose"] | int = None,
        metadata: bool = None,
        peak: Literal["none", "sample", "true"] = None,
        dualmono: bool = None,
        panlaw: float = None,
        target: int = None,
        gauge: Literal["momentary", "m", "shortterm", "s"] | int = None,
        scale: Literal["absolute", "LUFS", "relative", "LU"] | int = None,
        integrated: float = None,
        range: float = None,
        lra_low: float = None,
        lra_high: float = None,
        sample_peak: float = None,
        true_peak: float = None,
    ) -> "FilterMultiOutput":
        """EBU R128 scanner."""
        return self._apply_dynamic_outputs_filter(
            filter_name="ebur128",
            inputs=[self],
            named_arguments={
                "video": video,
                "size": size,
                "meter": meter,
                "framelog": framelog,
                "metadata": metadata,
                "peak": peak,
                "dualmono": dualmono,
                "panlaw": panlaw,
                "target": target,
                "gauge": gauge,
                "scale": scale,
                "integrated": integrated,
                "range": range,
                "lra_low": lra_low,
                "lra_high": lra_high,
                "sample_peak": sample_peak,
                "true_peak": true_peak,
            },
        )

    def edgedetect(
        self,
        high: float = None,
        low: float = None,
        mode: Literal["wires", "colormix", "canny"] | int = None,
        planes: Literal["y", "u", "v", "r", "g", "b"] = None,
    ) -> "Stream":
        """Detect and draw edge."""
        return self._apply_filter(
            filter_name="edgedetect",
            inputs=[self],
            named_arguments={
                "high": high,
                "low": low,
                "mode": mode,
                "planes": planes,
            },
        )[0]

    def elbg(
        self,
        codebook_length: int = None,
        l: int = None,
        nb_steps: int = None,
        n: int = None,
        seed: str = None,
        s: str = None,
        pal8: bool = None,
        use_alpha: bool = None,
    ) -> "Stream":
        """Apply posterize effect, using the ELBG algorithm."""
        return self._apply_filter(
            filter_name="elbg",
            inputs=[self],
            named_arguments={
                "codebook_length": codebook_length,
                "l": l,
                "nb_steps": nb_steps,
                "n": n,
                "seed": seed,
                "s": s,
                "pal8": pal8,
                "use_alpha": use_alpha,
            },
        )[0]

    def entropy(self, mode: Literal["normal", "diff"] | int = None) -> "Stream":
        """Measure video frames entropy."""
        return self._apply_filter(
            filter_name="entropy",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def epx(self, n: int = None) -> "Stream":
        """Scale the input using EPX algorithm."""
        return self._apply_filter(
            filter_name="epx",
            inputs=[self],
            named_arguments={
                "n": n,
            },
        )[0]

    def eq(
        self,
        contrast: str = None,
        brightness: str = None,
        saturation: str = None,
        gamma: str = None,
        gamma_r: str = None,
        gamma_g: str = None,
        gamma_b: str = None,
        gamma_weight: str = None,
        eval: Literal["init", "frame"] | int = None,
    ) -> "Stream":
        """Adjust brightness, contrast, gamma, and saturation."""
        return self._apply_filter(
            filter_name="eq",
            inputs=[self],
            named_arguments={
                "contrast": contrast,
                "brightness": brightness,
                "saturation": saturation,
                "gamma": gamma,
                "gamma_r": gamma_r,
                "gamma_g": gamma_g,
                "gamma_b": gamma_b,
                "gamma_weight": gamma_weight,
                "eval": eval,
            },
        )[0]

    def equalizer(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        gain: float = None,
        g: float = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply two-pole peaking equalization (EQ) filter."""
        return self._apply_filter(
            filter_name="equalizer",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def erosion(
        self,
        coordinates: int = None,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
    ) -> "Stream":
        """Apply erosion effect."""
        return self._apply_filter(
            filter_name="erosion",
            inputs=[self],
            named_arguments={
                "coordinates": coordinates,
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            },
        )[0]

    def estdif(
        self,
        mode: Literal["frame", "field"] | int = None,
        parity: Literal["tff", "bff", "auto"] | int = None,
        deint: Literal["all", "interlaced"] | int = None,
        rslope: int = None,
        redge: int = None,
        ecost: int = None,
        mcost: int = None,
        dcost: int = None,
        interp: Literal["2p", "4p", "6p"] | int = None,
    ) -> "Stream":
        """Apply Edge Slope Tracing deinterlace."""
        return self._apply_filter(
            filter_name="estdif",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "parity": parity,
                "deint": deint,
                "rslope": rslope,
                "redge": redge,
                "ecost": ecost,
                "mcost": mcost,
                "dcost": dcost,
                "interp": interp,
            },
        )[0]

    def exposure(self, exposure: float = None, black: float = None) -> "Stream":
        """Adjust exposure of the video stream."""
        return self._apply_filter(
            filter_name="exposure",
            inputs=[self],
            named_arguments={
                "exposure": exposure,
                "black": black,
            },
        )[0]

    def extractplanes(
        self, planes: Literal["y", "u", "v", "r", "g", "b", "a"] = None
    ) -> "FilterMultiOutput":
        """Extract planes as grayscale frames."""
        return self._apply_dynamic_outputs_filter(
            filter_name="extractplanes",
            inputs=[self],
            named_arguments={
                "planes": planes,
            },
        )

    def extrastereo(self, m: float = None, c: bool = None) -> "Stream":
        """Increase difference between stereo audio channels."""
        return self._apply_filter(
            filter_name="extrastereo",
            inputs=[self],
            named_arguments={
                "m": m,
                "c": c,
            },
        )[0]

    def fade(
        self,
        type: Literal["in", "out"] | int = None,
        t: Literal["in", "out"] | int = None,
        start_frame: int = None,
        s: int = None,
        nb_frames: int = None,
        n: int = None,
        alpha: bool = None,
        start_time: str = None,
        st: str = None,
        duration: str = None,
        d: str = None,
        color: str = None,
        c: str = None,
    ) -> "Stream":
        """Fade in/out input video."""
        return self._apply_filter(
            filter_name="fade",
            inputs=[self],
            named_arguments={
                "type": type,
                "t": t,
                "start_frame": start_frame,
                "s": s,
                "nb_frames": nb_frames,
                "n": n,
                "alpha": alpha,
                "start_time": start_time,
                "st": st,
                "duration": duration,
                "d": d,
                "color": color,
                "c": c,
            },
        )[0]

    def feedback(
        self,
        feedin_stream: "Stream",
        x: int = None,
        y: int = None,
        w: int = None,
        h: int = None,
    ) -> list["Stream"]:
        """Apply feedback video filter."""
        return self._apply_filter(
            filter_name="feedback",
            inputs=[self, feedin_stream],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
            },
            num_output_streams=2,
        )

    def fftdnoiz(
        self,
        sigma: float = None,
        amount: float = None,
        block: int = None,
        overlap: float = None,
        method: Literal["wiener", "hard"] | int = None,
        prev: int = None,
        next: int = None,
        planes: int = None,
        window: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
    ) -> "Stream":
        """Denoise frames using 3D FFT."""
        return self._apply_filter(
            filter_name="fftdnoiz",
            inputs=[self],
            named_arguments={
                "sigma": sigma,
                "amount": amount,
                "block": block,
                "overlap": overlap,
                "method": method,
                "prev": prev,
                "next": next,
                "planes": planes,
                "window": window,
            },
        )[0]

    def fftfilt(
        self,
        dc_Y: int = None,
        dc_U: int = None,
        dc_V: int = None,
        weight_Y: str = None,
        weight_U: str = None,
        weight_V: str = None,
        eval: Literal["init", "frame"] | int = None,
    ) -> "Stream":
        """Apply arbitrary expressions to pixels in frequency domain."""
        return self._apply_filter(
            filter_name="fftfilt",
            inputs=[self],
            named_arguments={
                "dc_Y": dc_Y,
                "dc_U": dc_U,
                "dc_V": dc_V,
                "weight_Y": weight_Y,
                "weight_U": weight_U,
                "weight_V": weight_V,
                "eval": eval,
            },
        )[0]

    def field(self, type: Literal["top", "bottom"] | int = None) -> "Stream":
        """Extract a field from the input video."""
        return self._apply_filter(
            filter_name="field",
            inputs=[self],
            named_arguments={
                "type": type,
            },
        )[0]

    def fieldhint(
        self,
        hint: str = None,
        mode: Literal["absolute", "relative", "pattern"] | int = None,
    ) -> "Stream":
        """Field matching using hints."""
        return self._apply_filter(
            filter_name="fieldhint",
            inputs=[self],
            named_arguments={
                "hint": hint,
                "mode": mode,
            },
        )[0]

    def fieldmatch(
        self,
        *streams: "Stream",
        order: Literal["auto", "bff", "tff"] | int = None,
        mode: Literal["pc", "pc_n", "pc_u", "pc_n_ub", "pcn", "pcn_ub"] | int = None,
        ppsrc: bool = None,
        field: Literal["auto", "bottom", "top"] | int = None,
        mchroma: bool = None,
        y0: int = None,
        y1: int = None,
        scthresh: float = None,
        combmatch: Literal["none", "sc", "full"] | int = None,
        combdbg: Literal["none", "pcn", "pcnub"] | int = None,
        cthresh: int = None,
        chroma: bool = None,
        blockx: int = None,
        blocky: int = None,
        combpel: int = None,
    ) -> "Stream":
        """Field matching for inverse telecine."""
        return self._apply_filter(
            filter_name="fieldmatch",
            inputs=[self, *streams],
            named_arguments={
                "order": order,
                "mode": mode,
                "ppsrc": ppsrc,
                "field": field,
                "mchroma": mchroma,
                "y0": y0,
                "y1": y1,
                "scthresh": scthresh,
                "combmatch": combmatch,
                "combdbg": combdbg,
                "cthresh": cthresh,
                "chroma": chroma,
                "blockx": blockx,
                "blocky": blocky,
                "combpel": combpel,
            },
        )[0]

    def fieldorder(self, order: Literal["bff", "tff"] | int = None) -> "Stream":
        """Set the field order."""
        return self._apply_filter(
            filter_name="fieldorder",
            inputs=[self],
            named_arguments={
                "order": order,
            },
        )[0]

    def fillborders(
        self,
        left: int = None,
        right: int = None,
        top: int = None,
        bottom: int = None,
        mode: Literal["smear", "mirror", "fixed", "reflect", "wrap", "fade", "margins"]
        | int = None,
        color: str = None,
    ) -> "Stream":
        """Fill borders of the input video."""
        return self._apply_filter(
            filter_name="fillborders",
            inputs=[self],
            named_arguments={
                "left": left,
                "right": right,
                "top": top,
                "bottom": bottom,
                "mode": mode,
                "color": color,
            },
        )[0]

    def find_rect(
        self,
        object: str = None,
        threshold: float = None,
        mipmaps: int = None,
        xmin: int = None,
        ymin: int = None,
        xmax: int = None,
        ymax: int = None,
        discard: bool = None,
    ) -> "Stream":
        """Find a user specified object."""
        return self._apply_filter(
            filter_name="find_rect",
            inputs=[self],
            named_arguments={
                "object": object,
                "threshold": threshold,
                "mipmaps": mipmaps,
                "xmin": xmin,
                "ymin": ymin,
                "xmax": xmax,
                "ymax": ymax,
                "discard": discard,
            },
        )[0]

    def firequalizer(
        self,
        gain: str = None,
        gain_entry: str = None,
        delay: float = None,
        accuracy: float = None,
        wfunc: Literal[
            "rectangular",
            "hann",
            "hamming",
            "blackman",
            "nuttall3",
            "mnuttall3",
            "nuttall",
            "bnuttall",
            "bharris",
            "tukey",
        ]
        | int = None,
        fixed: bool = None,
        multi: bool = None,
        zero_phase: bool = None,
        scale: Literal["linlin", "linlog", "loglin", "loglog"] | int = None,
        dumpfile: str = None,
        dumpscale: Literal["linlin", "linlog", "loglin", "loglog"] | int = None,
        fft2: bool = None,
        min_phase: bool = None,
    ) -> "Stream":
        """Finite Impulse Response Equalizer."""
        return self._apply_filter(
            filter_name="firequalizer",
            inputs=[self],
            named_arguments={
                "gain": gain,
                "gain_entry": gain_entry,
                "delay": delay,
                "accuracy": accuracy,
                "wfunc": wfunc,
                "fixed": fixed,
                "multi": multi,
                "zero_phase": zero_phase,
                "scale": scale,
                "dumpfile": dumpfile,
                "dumpscale": dumpscale,
                "fft2": fft2,
                "min_phase": min_phase,
            },
        )[0]

    def flanger(
        self,
        delay: float = None,
        depth: float = None,
        regen: float = None,
        width: float = None,
        speed: float = None,
        shape: Literal["triangular", "t", "sinusoidal", "s"] | int = None,
        phase: float = None,
        interp: Literal["linear", "quadratic"] | int = None,
    ) -> "Stream":
        """Apply a flanging effect to the audio."""
        return self._apply_filter(
            filter_name="flanger",
            inputs=[self],
            named_arguments={
                "delay": delay,
                "depth": depth,
                "regen": regen,
                "width": width,
                "speed": speed,
                "shape": shape,
                "phase": phase,
                "interp": interp,
            },
        )[0]

    def floodfill(
        self,
        x: int = None,
        y: int = None,
        s0: int = None,
        s1: int = None,
        s2: int = None,
        s3: int = None,
        d0: int = None,
        d1: int = None,
        d2: int = None,
        d3: int = None,
    ) -> "Stream":
        """Fill area with same color with another color."""
        return self._apply_filter(
            filter_name="floodfill",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "s0": s0,
                "s1": s1,
                "s2": s2,
                "s3": s3,
                "d0": d0,
                "d1": d1,
                "d2": d2,
                "d3": d3,
            },
        )[0]

    def format(
        self, pix_fmts: str = None, color_spaces: str = None, color_ranges: str = None
    ) -> "Stream":
        """Convert the input video to one of the specified pixel formats."""
        return self._apply_filter(
            filter_name="format",
            inputs=[self],
            named_arguments={
                "pix_fmts": pix_fmts,
                "color_spaces": color_spaces,
                "color_ranges": color_ranges,
            },
        )[0]

    def fps(
        self,
        fps: str = None,
        start_time: float = None,
        round: Literal["zero", "inf", "down", "up", "near"] | int = None,
        eof_action: Literal["round", "pass"] | int = None,
    ) -> "Stream":
        """Force constant framerate."""
        return self._apply_filter(
            filter_name="fps",
            inputs=[self],
            named_arguments={
                "fps": fps,
                "start_time": start_time,
                "round": round,
                "eof_action": eof_action,
            },
        )[0]

    def framepack(
        self,
        right_stream: "Stream",
        format: Literal["sbs", "tab", "frameseq", "lines", "columns"] | int = None,
    ) -> "Stream":
        """Generate a frame packed stereoscopic video."""
        return self._apply_filter(
            filter_name="framepack",
            inputs=[self, right_stream],
            named_arguments={
                "format": format,
            },
        )[0]

    def framerate(
        self,
        fps: str = None,
        interp_start: int = None,
        interp_end: int = None,
        scene: float = None,
        flags: Literal["scene_change_detect", "scd"] = None,
    ) -> "Stream":
        """Upsamples or downsamples progressive source between specified frame rates."""
        return self._apply_filter(
            filter_name="framerate",
            inputs=[self],
            named_arguments={
                "fps": fps,
                "interp_start": interp_start,
                "interp_end": interp_end,
                "scene": scene,
                "flags": flags,
            },
        )[0]

    def framestep(self, step: int = None) -> "Stream":
        """Select one frame every N frames."""
        return self._apply_filter(
            filter_name="framestep",
            inputs=[self],
            named_arguments={
                "step": step,
            },
        )[0]

    def freezedetect(
        self, n: float = None, noise: float = None, d: str = None, duration: str = None
    ) -> "Stream":
        """Detects frozen video input."""
        return self._apply_filter(
            filter_name="freezedetect",
            inputs=[self],
            named_arguments={
                "n": n,
                "noise": noise,
                "d": d,
                "duration": duration,
            },
        )[0]

    def freezeframes(
        self,
        replace_stream: "Stream",
        first: str = None,
        last: str = None,
        replace: str = None,
    ) -> "Stream":
        """Freeze video frames."""
        return self._apply_filter(
            filter_name="freezeframes",
            inputs=[self, replace_stream],
            named_arguments={
                "first": first,
                "last": last,
                "replace": replace,
            },
        )[0]

    def frei0r(self, filter_name: str = None, filter_params: str = None) -> "Stream":
        """Apply a frei0r effect."""
        return self._apply_filter(
            filter_name="frei0r",
            inputs=[self],
            named_arguments={
                "filter_name": filter_name,
                "filter_params": filter_params,
            },
        )[0]

    def fspp(
        self,
        quality: int = None,
        qp: int = None,
        strength: int = None,
        use_bframe_qp: bool = None,
    ) -> "Stream":
        """Apply Fast Simple Post-processing filter."""
        return self._apply_filter(
            filter_name="fspp",
            inputs=[self],
            named_arguments={
                "quality": quality,
                "qp": qp,
                "strength": strength,
                "use_bframe_qp": use_bframe_qp,
            },
        )[0]

    def fsync(self, file: str = None, f: str = None) -> "Stream":
        """Synchronize video frames from external source."""
        return self._apply_filter(
            filter_name="fsync",
            inputs=[self],
            named_arguments={
                "file": file,
                "f": f,
            },
        )[0]

    def gblur(
        self,
        sigma: float = None,
        steps: int = None,
        planes: int = None,
        sigmaV: float = None,
    ) -> "Stream":
        """Apply Gaussian Blur filter."""
        return self._apply_filter(
            filter_name="gblur",
            inputs=[self],
            named_arguments={
                "sigma": sigma,
                "steps": steps,
                "planes": planes,
                "sigmaV": sigmaV,
            },
        )[0]

    def geq(
        self,
        lum_expr: str = None,
        lum: str = None,
        cb_expr: str = None,
        cb: str = None,
        cr_expr: str = None,
        cr: str = None,
        alpha_expr: str = None,
        a: str = None,
        red_expr: str = None,
        r: str = None,
        green_expr: str = None,
        g: str = None,
        blue_expr: str = None,
        b: str = None,
        interpolation: Literal["nearest", "n", "bilinear", "b"] | int = None,
        i: Literal["nearest", "n", "bilinear", "b"] | int = None,
    ) -> "Stream":
        """Apply generic equation to each pixel."""
        return self._apply_filter(
            filter_name="geq",
            inputs=[self],
            named_arguments={
                "lum_expr": lum_expr,
                "lum": lum,
                "cb_expr": cb_expr,
                "cb": cb,
                "cr_expr": cr_expr,
                "cr": cr,
                "alpha_expr": alpha_expr,
                "a": a,
                "red_expr": red_expr,
                "r": r,
                "green_expr": green_expr,
                "g": g,
                "blue_expr": blue_expr,
                "b": b,
                "interpolation": interpolation,
                "i": i,
            },
        )[0]

    def gradfun(self, strength: float = None, radius: int = None) -> "Stream":
        """Debands video quickly using gradients."""
        return self._apply_filter(
            filter_name="gradfun",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "radius": radius,
            },
        )[0]

    def graphmonitor(
        self,
        size: str = None,
        s: str = None,
        opacity: float = None,
        o: float = None,
        mode: Literal["full", "compact", "nozero", "noeof", "nodisabled"] = None,
        m: Literal["full", "compact", "nozero", "noeof", "nodisabled"] = None,
        flags: Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ] = None,
        f: Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ] = None,
        rate: str = None,
        r: str = None,
    ) -> "Stream":
        """Show various filtergraph stats."""
        return self._apply_filter(
            filter_name="graphmonitor",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "opacity": opacity,
                "o": o,
                "mode": mode,
                "m": m,
                "flags": flags,
                "f": f,
                "rate": rate,
                "r": r,
            },
        )[0]

    def grayworld(self) -> "Stream":
        """Adjust white balance using LAB gray world algorithm"""
        return self._apply_filter(
            filter_name="grayworld", inputs=[self], named_arguments={}
        )[0]

    def greyedge(
        self, difford: int = None, minknorm: int = None, sigma: float = None
    ) -> "Stream":
        """Estimates scene illumination by grey edge assumption."""
        return self._apply_filter(
            filter_name="greyedge",
            inputs=[self],
            named_arguments={
                "difford": difford,
                "minknorm": minknorm,
                "sigma": sigma,
            },
        )[0]

    def guided(
        self,
        *streams: "Stream",
        radius: int = None,
        eps: float = None,
        mode: Literal["basic", "fast"] | int = None,
        sub: int = None,
        guidance: Literal["off", "on"] | int = None,
        planes: int = None,
    ) -> "Stream":
        """Apply Guided filter."""
        return self._apply_filter(
            filter_name="guided",
            inputs=[self, *streams],
            named_arguments={
                "radius": radius,
                "eps": eps,
                "mode": mode,
                "sub": sub,
                "guidance": guidance,
                "planes": planes,
            },
        )[0]

    def haas(
        self,
        level_in: float = None,
        level_out: float = None,
        side_gain: float = None,
        middle_source: Literal["left", "right", "mid", "side"] | int = None,
        middle_phase: bool = None,
        left_delay: float = None,
        left_balance: float = None,
        left_gain: float = None,
        left_phase: bool = None,
        right_delay: float = None,
        right_balance: float = None,
        right_gain: float = None,
        right_phase: bool = None,
    ) -> "Stream":
        """Apply Haas Stereo Enhancer."""
        return self._apply_filter(
            filter_name="haas",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "side_gain": side_gain,
                "middle_source": middle_source,
                "middle_phase": middle_phase,
                "left_delay": left_delay,
                "left_balance": left_balance,
                "left_gain": left_gain,
                "left_phase": left_phase,
                "right_delay": right_delay,
                "right_balance": right_balance,
                "right_gain": right_gain,
                "right_phase": right_phase,
            },
        )[0]

    def haldclut(
        self,
        clut_stream: "Stream",
        clut: Literal["first", "all"] | int = None,
        interp: Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | int = None,
    ) -> "Stream":
        """Adjust colors using a Hald CLUT."""
        return self._apply_filter(
            filter_name="haldclut",
            inputs=[self, clut_stream],
            named_arguments={
                "clut": clut,
                "interp": interp,
            },
        )[0]

    def hdcd(
        self,
        disable_autoconvert: bool = None,
        process_stereo: bool = None,
        cdt_ms: int = None,
        force_pe: bool = None,
        analyze_mode: Literal["off", "lle", "pe", "cdt", "tgm"] | int = None,
        bits_per_sample: Literal["16", "20", "24"] | int = None,
    ) -> "Stream":
        """Apply High Definition Compatible Digital (HDCD) decoding."""
        return self._apply_filter(
            filter_name="hdcd",
            inputs=[self],
            named_arguments={
                "disable_autoconvert": disable_autoconvert,
                "process_stereo": process_stereo,
                "cdt_ms": cdt_ms,
                "force_pe": force_pe,
                "analyze_mode": analyze_mode,
                "bits_per_sample": bits_per_sample,
            },
        )[0]

    def headphone(
        self,
        *streams: "Stream",
        map: str = None,
        gain: float = None,
        lfe: float = None,
        type: Literal["time", "freq"] | int = None,
        size: int = None,
        hrir: Literal["stereo", "multich"] | int = None,
    ) -> "Stream":
        """Apply headphone binaural spatialization with HRTFs in additional streams."""
        return self._apply_filter(
            filter_name="headphone",
            inputs=[self, *streams],
            named_arguments={
                "map": map,
                "gain": gain,
                "lfe": lfe,
                "type": type,
                "size": size,
                "hrir": hrir,
            },
        )[0]

    def hflip(self) -> "Stream":
        """Horizontally flip the input video."""
        return self._apply_filter(
            filter_name="hflip", inputs=[self], named_arguments={}
        )[0]

    def highpass(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        poles: int = None,
        p: int = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply a high-pass filter with 3dB point frequency."""
        return self._apply_filter(
            filter_name="highpass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def highshelf(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        gain: float = None,
        g: float = None,
        poles: int = None,
        p: int = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply a high shelf filter."""
        return self._apply_filter(
            filter_name="highshelf",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def histeq(
        self,
        strength: float = None,
        intensity: float = None,
        antibanding: Literal["none", "weak", "strong"] | int = None,
    ) -> "Stream":
        """Apply global color histogram equalization."""
        return self._apply_filter(
            filter_name="histeq",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "intensity": intensity,
                "antibanding": antibanding,
            },
        )[0]

    def histogram(
        self,
        level_height: int = None,
        scale_height: int = None,
        display_mode: Literal["overlay", "parade", "stack"] | int = None,
        d: Literal["overlay", "parade", "stack"] | int = None,
        levels_mode: Literal["linear", "logarithmic"] | int = None,
        m: Literal["linear", "logarithmic"] | int = None,
        components: int = None,
        c: int = None,
        fgopacity: float = None,
        f: float = None,
        bgopacity: float = None,
        b: float = None,
        colors_mode: Literal[
            "whiteonblack",
            "blackonwhite",
            "whiteongray",
            "blackongray",
            "coloronblack",
            "coloronwhite",
            "colorongray",
            "blackoncolor",
            "whiteoncolor",
            "grayoncolor",
        ]
        | int = None,
        l: Literal[
            "whiteonblack",
            "blackonwhite",
            "whiteongray",
            "blackongray",
            "coloronblack",
            "coloronwhite",
            "colorongray",
            "blackoncolor",
            "whiteoncolor",
            "grayoncolor",
        ]
        | int = None,
    ) -> "Stream":
        """Compute and draw a histogram."""
        return self._apply_filter(
            filter_name="histogram",
            inputs=[self],
            named_arguments={
                "level_height": level_height,
                "scale_height": scale_height,
                "display_mode": display_mode,
                "d": d,
                "levels_mode": levels_mode,
                "m": m,
                "components": components,
                "c": c,
                "fgopacity": fgopacity,
                "f": f,
                "bgopacity": bgopacity,
                "b": b,
                "colors_mode": colors_mode,
                "l": l,
            },
        )[0]

    def hqdn3d(
        self,
        luma_spatial: float = None,
        chroma_spatial: float = None,
        luma_tmp: float = None,
        chroma_tmp: float = None,
    ) -> "Stream":
        """Apply a High Quality 3D Denoiser."""
        return self._apply_filter(
            filter_name="hqdn3d",
            inputs=[self],
            named_arguments={
                "luma_spatial": luma_spatial,
                "chroma_spatial": chroma_spatial,
                "luma_tmp": luma_tmp,
                "chroma_tmp": chroma_tmp,
            },
        )[0]

    def hqx(self, n: int = None) -> "Stream":
        """Scale the input by 2, 3 or 4 using the hq*x magnification algorithm."""
        return self._apply_filter(
            filter_name="hqx",
            inputs=[self],
            named_arguments={
                "n": n,
            },
        )[0]

    def hstack(
        self, *streams: "Stream", inputs: int = None, shortest: bool = None
    ) -> "Stream":
        """Stack video inputs horizontally."""
        return self._apply_filter(
            filter_name="hstack",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "shortest": shortest,
            },
        )[0]

    def hsvhold(
        self,
        hue: float = None,
        sat: float = None,
        val: float = None,
        similarity: float = None,
        blend: float = None,
    ) -> "Stream":
        """Turns a certain HSV range into gray."""
        return self._apply_filter(
            filter_name="hsvhold",
            inputs=[self],
            named_arguments={
                "hue": hue,
                "sat": sat,
                "val": val,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def hsvkey(
        self,
        hue: float = None,
        sat: float = None,
        val: float = None,
        similarity: float = None,
        blend: float = None,
    ) -> "Stream":
        """Turns a certain HSV range into transparency. Operates on YUV colors."""
        return self._apply_filter(
            filter_name="hsvkey",
            inputs=[self],
            named_arguments={
                "hue": hue,
                "sat": sat,
                "val": val,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def hue(
        self, h: str = None, s: str = None, H: str = None, b: str = None
    ) -> "Stream":
        """Adjust the hue and saturation of the input video."""
        return self._apply_filter(
            filter_name="hue",
            inputs=[self],
            named_arguments={
                "h": h,
                "s": s,
                "H": H,
                "b": b,
            },
        )[0]

    def huesaturation(
        self,
        hue: float = None,
        saturation: float = None,
        intensity: float = None,
        colors: Literal["r", "y", "g", "c", "b", "m", "a"] = None,
        strength: float = None,
        rw: float = None,
        gw: float = None,
        bw: float = None,
        lightness: bool = None,
    ) -> "Stream":
        """Apply hue-saturation-intensity adjustments."""
        return self._apply_filter(
            filter_name="huesaturation",
            inputs=[self],
            named_arguments={
                "hue": hue,
                "saturation": saturation,
                "intensity": intensity,
                "colors": colors,
                "strength": strength,
                "rw": rw,
                "gw": gw,
                "bw": bw,
                "lightness": lightness,
            },
        )[0]

    def hwdownload(self) -> "Stream":
        """Download a hardware frame to a normal frame"""
        return self._apply_filter(
            filter_name="hwdownload", inputs=[self], named_arguments={}
        )[0]

    def hwmap(
        self,
        mode: Literal["read", "write", "overwrite", "direct"] = None,
        derive_device: str = None,
        reverse: int = None,
    ) -> "Stream":
        """Map hardware frames"""
        return self._apply_filter(
            filter_name="hwmap",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "derive_device": derive_device,
                "reverse": reverse,
            },
        )[0]

    def hwupload(self, derive_device: str = None) -> "Stream":
        """Upload a normal frame to a hardware frame"""
        return self._apply_filter(
            filter_name="hwupload",
            inputs=[self],
            named_arguments={
                "derive_device": derive_device,
            },
        )[0]

    def hysteresis(
        self, alt_stream: "Stream", planes: int = None, threshold: int = None
    ) -> "Stream":
        """Grow first stream into second stream by connecting components."""
        return self._apply_filter(
            filter_name="hysteresis",
            inputs=[self, alt_stream],
            named_arguments={
                "planes": planes,
                "threshold": threshold,
            },
        )[0]

    def identity(self, reference_stream: "Stream") -> "Stream":
        """Calculate the Identity between two video streams."""
        return self._apply_filter(
            filter_name="identity", inputs=[self, reference_stream], named_arguments={}
        )[0]

    def idet(
        self,
        intl_thres: float = None,
        prog_thres: float = None,
        rep_thres: float = None,
        half_life: float = None,
        analyze_interlaced_flag: int = None,
    ) -> "Stream":
        """Interlace detect Filter."""
        return self._apply_filter(
            filter_name="idet",
            inputs=[self],
            named_arguments={
                "intl_thres": intl_thres,
                "prog_thres": prog_thres,
                "rep_thres": rep_thres,
                "half_life": half_life,
                "analyze_interlaced_flag": analyze_interlaced_flag,
            },
        )[0]

    def il(
        self,
        luma_mode: Literal["none", "interleave", "i", "deinterleave", "d"] | int = None,
        l: Literal["none", "interleave", "i", "deinterleave", "d"] | int = None,
        chroma_mode: Literal["none", "interleave", "i", "deinterleave", "d"]
        | int = None,
        c: Literal["none", "interleave", "i", "deinterleave", "d"] | int = None,
        alpha_mode: Literal["none", "interleave", "i", "deinterleave", "d"]
        | int = None,
        a: Literal["none", "interleave", "i", "deinterleave", "d"] | int = None,
        luma_swap: bool = None,
        ls: bool = None,
        chroma_swap: bool = None,
        cs: bool = None,
        alpha_swap: bool = None,
        as_: bool = None,
    ) -> "Stream":
        """Deinterleave or interleave fields."""
        return self._apply_filter(
            filter_name="il",
            inputs=[self],
            named_arguments={
                "luma_mode": luma_mode,
                "l": l,
                "chroma_mode": chroma_mode,
                "c": c,
                "alpha_mode": alpha_mode,
                "a": a,
                "luma_swap": luma_swap,
                "ls": ls,
                "chroma_swap": chroma_swap,
                "cs": cs,
                "alpha_swap": alpha_swap,
                "as": as_,
            },
        )[0]

    def inflate(
        self,
        threshold0: int = None,
        threshold1: int = None,
        threshold2: int = None,
        threshold3: int = None,
    ) -> "Stream":
        """Apply inflate effect."""
        return self._apply_filter(
            filter_name="inflate",
            inputs=[self],
            named_arguments={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            },
        )[0]

    def interlace(
        self,
        scan: Literal["tff", "bff"] | int = None,
        lowpass: Literal["off", "linear", "complex"] | int = None,
    ) -> "Stream":
        """Convert progressive video into interlaced."""
        return self._apply_filter(
            filter_name="interlace",
            inputs=[self],
            named_arguments={
                "scan": scan,
                "lowpass": lowpass,
            },
        )[0]

    def interleave(
        self,
        *streams: "Stream",
        nb_inputs: int = None,
        n: int = None,
        duration: Literal["longest", "shortest", "first"] | int = None,
    ) -> "Stream":
        """Temporally interleave video inputs."""
        return self._apply_filter(
            filter_name="interleave",
            inputs=[self, *streams],
            named_arguments={
                "nb_inputs": nb_inputs,
                "n": n,
                "duration": duration,
            },
        )[0]

    def join(
        self,
        *streams: "Stream",
        inputs: int = None,
        channel_layout: str = None,
        map: str = None,
    ) -> "Stream":
        """Join multiple audio streams into multi-channel output."""
        return self._apply_filter(
            filter_name="join",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "channel_layout": channel_layout,
                "map": map,
            },
        )[0]

    def kerndeint(
        self,
        thresh: int = None,
        map: bool = None,
        order: bool = None,
        sharp: bool = None,
        twoway: bool = None,
    ) -> "Stream":
        """Apply kernel deinterlacing to the input."""
        return self._apply_filter(
            filter_name="kerndeint",
            inputs=[self],
            named_arguments={
                "thresh": thresh,
                "map": map,
                "order": order,
                "sharp": sharp,
                "twoway": twoway,
            },
        )[0]

    def kirsch(
        self, planes: int = None, scale: float = None, delta: float = None
    ) -> "Stream":
        """Apply kirsch operator."""
        return self._apply_filter(
            filter_name="kirsch",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def lagfun(self, decay: float = None, planes: str = None) -> "Stream":
        """Slowly update darker pixels."""
        return self._apply_filter(
            filter_name="lagfun",
            inputs=[self],
            named_arguments={
                "decay": decay,
                "planes": planes,
            },
        )[0]

    def latency(self) -> "Stream":
        """Report video filtering latency."""
        return self._apply_filter(
            filter_name="latency", inputs=[self], named_arguments={}
        )[0]

    def lenscorrection(
        self,
        cx: float = None,
        cy: float = None,
        k1: float = None,
        k2: float = None,
        i: Literal["nearest", "bilinear"] | int = None,
        fc: str = None,
    ) -> "Stream":
        """Rectify the image by correcting for lens distortion."""
        return self._apply_filter(
            filter_name="lenscorrection",
            inputs=[self],
            named_arguments={
                "cx": cx,
                "cy": cy,
                "k1": k1,
                "k2": k2,
                "i": i,
                "fc": fc,
            },
        )[0]

    def libvmaf(
        self,
        reference_stream: "Stream",
        log_path: str = None,
        log_fmt: str = None,
        pool: str = None,
        n_threads: int = None,
        n_subsample: int = None,
        model: str = None,
        feature: str = None,
    ) -> "Stream":
        """Calculate the VMAF between two video streams."""
        return self._apply_filter(
            filter_name="libvmaf",
            inputs=[self, reference_stream],
            named_arguments={
                "log_path": log_path,
                "log_fmt": log_fmt,
                "pool": pool,
                "n_threads": n_threads,
                "n_subsample": n_subsample,
                "model": model,
                "feature": feature,
            },
        )[0]

    def limitdiff(
        self,
        *streams: "Stream",
        threshold: float = None,
        elasticity: float = None,
        reference: bool = None,
        planes: int = None,
    ) -> "Stream":
        """Apply filtering with limiting difference."""
        return self._apply_filter(
            filter_name="limitdiff",
            inputs=[self, *streams],
            named_arguments={
                "threshold": threshold,
                "elasticity": elasticity,
                "reference": reference,
                "planes": planes,
            },
        )[0]

    def limiter(self, min: int = None, max: int = None, planes: int = None) -> "Stream":
        """Limit pixels components to the specified range."""
        return self._apply_filter(
            filter_name="limiter",
            inputs=[self],
            named_arguments={
                "min": min,
                "max": max,
                "planes": planes,
            },
        )[0]

    def loop(
        self, loop: int = None, size: str = None, start: str = None, time: str = None
    ) -> "Stream":
        """Loop video frames."""
        return self._apply_filter(
            filter_name="loop",
            inputs=[self],
            named_arguments={
                "loop": loop,
                "size": size,
                "start": start,
                "time": time,
            },
        )[0]

    def loudnorm(
        self,
        I: float = None,
        i: float = None,
        LRA: float = None,
        lra: float = None,
        TP: float = None,
        tp: float = None,
        measured_I: float = None,
        measured_i: float = None,
        measured_LRA: float = None,
        measured_lra: float = None,
        measured_TP: float = None,
        measured_tp: float = None,
        measured_thresh: float = None,
        offset: float = None,
        linear: bool = None,
        dual_mono: bool = None,
        print_format: Literal["none", "json", "summary"] | int = None,
    ) -> "Stream":
        """EBU R128 loudness normalization"""
        return self._apply_filter(
            filter_name="loudnorm",
            inputs=[self],
            named_arguments={
                "I": I,
                "i": i,
                "LRA": LRA,
                "lra": lra,
                "TP": TP,
                "tp": tp,
                "measured_I": measured_I,
                "measured_i": measured_i,
                "measured_LRA": measured_LRA,
                "measured_lra": measured_lra,
                "measured_TP": measured_TP,
                "measured_tp": measured_tp,
                "measured_thresh": measured_thresh,
                "offset": offset,
                "linear": linear,
                "dual_mono": dual_mono,
                "print_format": print_format,
            },
        )[0]

    def lowpass(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        poles: int = None,
        p: int = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply a low-pass filter with 3dB point frequency."""
        return self._apply_filter(
            filter_name="lowpass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def lowshelf(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        gain: float = None,
        g: float = None,
        poles: int = None,
        p: int = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply a low shelf filter."""
        return self._apply_filter(
            filter_name="lowshelf",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def lumakey(
        self, threshold: float = None, tolerance: float = None, softness: float = None
    ) -> "Stream":
        """Turns a certain luma into transparency."""
        return self._apply_filter(
            filter_name="lumakey",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "tolerance": tolerance,
                "softness": softness,
            },
        )[0]

    def lut(
        self,
        c0: str = None,
        c1: str = None,
        c2: str = None,
        c3: str = None,
        y: str = None,
        u: str = None,
        v: str = None,
        r: str = None,
        g: str = None,
        b: str = None,
        a: str = None,
    ) -> "Stream":
        """Compute and apply a lookup table to the RGB/YUV input video."""
        return self._apply_filter(
            filter_name="lut",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "y": y,
                "u": u,
                "v": v,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
            },
        )[0]

    def lut1d(
        self,
        file: str = None,
        interp: Literal["nearest", "linear", "cosine", "cubic", "spline"] | int = None,
    ) -> "Stream":
        """Adjust colors using a 1D LUT."""
        return self._apply_filter(
            filter_name="lut1d",
            inputs=[self],
            named_arguments={
                "file": file,
                "interp": interp,
            },
        )[0]

    def lut2(
        self,
        srcy_stream: "Stream",
        c0: str = None,
        c1: str = None,
        c2: str = None,
        c3: str = None,
        d: int = None,
    ) -> "Stream":
        """Compute and apply a lookup table from two video inputs."""
        return self._apply_filter(
            filter_name="lut2",
            inputs=[self, srcy_stream],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "d": d,
            },
        )[0]

    def lut3d(
        self,
        file: str = None,
        clut: Literal["first", "all"] | int = None,
        interp: Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | int = None,
    ) -> "Stream":
        """Adjust colors using a 3D LUT."""
        return self._apply_filter(
            filter_name="lut3d",
            inputs=[self],
            named_arguments={
                "file": file,
                "clut": clut,
                "interp": interp,
            },
        )[0]

    def lutrgb(
        self,
        c0: str = None,
        c1: str = None,
        c2: str = None,
        c3: str = None,
        y: str = None,
        u: str = None,
        v: str = None,
        r: str = None,
        g: str = None,
        b: str = None,
        a: str = None,
    ) -> "Stream":
        """Compute and apply a lookup table to the RGB input video."""
        return self._apply_filter(
            filter_name="lutrgb",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "y": y,
                "u": u,
                "v": v,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
            },
        )[0]

    def lutyuv(
        self,
        c0: str = None,
        c1: str = None,
        c2: str = None,
        c3: str = None,
        y: str = None,
        u: str = None,
        v: str = None,
        r: str = None,
        g: str = None,
        b: str = None,
        a: str = None,
    ) -> "Stream":
        """Compute and apply a lookup table to the YUV input video."""
        return self._apply_filter(
            filter_name="lutyuv",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "y": y,
                "u": u,
                "v": v,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
            },
        )[0]

    def maskedclamp(
        self,
        dark_stream: "Stream",
        bright_stream: "Stream",
        undershoot: int = None,
        overshoot: int = None,
        planes: int = None,
    ) -> "Stream":
        """Clamp first stream with second stream and third stream."""
        return self._apply_filter(
            filter_name="maskedclamp",
            inputs=[self, dark_stream, bright_stream],
            named_arguments={
                "undershoot": undershoot,
                "overshoot": overshoot,
                "planes": planes,
            },
        )[0]

    def maskedmax(
        self, filter1_stream: "Stream", filter2_stream: "Stream", planes: int = None
    ) -> "Stream":
        """Apply filtering with maximum difference of two streams."""
        return self._apply_filter(
            filter_name="maskedmax",
            inputs=[self, filter1_stream, filter2_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def maskedmerge(
        self, overlay_stream: "Stream", mask_stream: "Stream", planes: int = None
    ) -> "Stream":
        """Merge first stream with second stream using third stream as mask."""
        return self._apply_filter(
            filter_name="maskedmerge",
            inputs=[self, overlay_stream, mask_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def maskedmin(
        self, filter1_stream: "Stream", filter2_stream: "Stream", planes: int = None
    ) -> "Stream":
        """Apply filtering with minimum difference of two streams."""
        return self._apply_filter(
            filter_name="maskedmin",
            inputs=[self, filter1_stream, filter2_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def maskedthreshold(
        self,
        reference_stream: "Stream",
        threshold: int = None,
        planes: int = None,
        mode: Literal["abs", "diff"] | int = None,
    ) -> "Stream":
        """Pick pixels comparing absolute difference of two streams with threshold."""
        return self._apply_filter(
            filter_name="maskedthreshold",
            inputs=[self, reference_stream],
            named_arguments={
                "threshold": threshold,
                "planes": planes,
                "mode": mode,
            },
        )[0]

    def maskfun(
        self,
        low: int = None,
        high: int = None,
        planes: int = None,
        fill: int = None,
        sum: int = None,
    ) -> "Stream":
        """Create Mask."""
        return self._apply_filter(
            filter_name="maskfun",
            inputs=[self],
            named_arguments={
                "low": low,
                "high": high,
                "planes": planes,
                "fill": fill,
                "sum": sum,
            },
        )[0]

    def mcdeint(
        self,
        mode: Literal["fast", "medium", "slow", "extra_slow"] | int = None,
        parity: Literal["tff", "bff"] | int = None,
        qp: int = None,
    ) -> "Stream":
        """Apply motion compensating deinterlacing."""
        return self._apply_filter(
            filter_name="mcdeint",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "parity": parity,
                "qp": qp,
            },
        )[0]

    def mcompand(self, args: str = None) -> "Stream":
        """Multiband Compress or expand audio dynamic range."""
        return self._apply_filter(
            filter_name="mcompand",
            inputs=[self],
            named_arguments={
                "args": args,
            },
        )[0]

    def median(
        self,
        radius: int = None,
        planes: int = None,
        radiusV: int = None,
        percentile: float = None,
    ) -> "Stream":
        """Apply Median filter."""
        return self._apply_filter(
            filter_name="median",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "planes": planes,
                "radiusV": radiusV,
                "percentile": percentile,
            },
        )[0]

    def mergeplanes(
        self,
        *streams: "Stream",
        mapping: int = None,
        format: str = None,
        map0s: int = None,
        map0p: int = None,
        map1s: int = None,
        map1p: int = None,
        map2s: int = None,
        map2p: int = None,
        map3s: int = None,
        map3p: int = None,
    ) -> "Stream":
        """Merge planes."""
        return self._apply_filter(
            filter_name="mergeplanes",
            inputs=[self, *streams],
            named_arguments={
                "mapping": mapping,
                "format": format,
                "map0s": map0s,
                "map0p": map0p,
                "map1s": map1s,
                "map1p": map1p,
                "map2s": map2s,
                "map2p": map2p,
                "map3s": map3s,
                "map3p": map3p,
            },
        )[0]

    def mestimate(
        self,
        method: Literal[
            "esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"
        ]
        | int = None,
        mb_size: int = None,
        search_param: int = None,
    ) -> "Stream":
        """Generate motion vectors."""
        return self._apply_filter(
            filter_name="mestimate",
            inputs=[self],
            named_arguments={
                "method": method,
                "mb_size": mb_size,
                "search_param": search_param,
            },
        )[0]

    def metadata(
        self,
        mode: Literal["select", "add", "modify", "delete", "print"] | int = None,
        key: str = None,
        value: str = None,
        function: Literal[
            "same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"
        ]
        | int = None,
        expr: str = None,
        file: str = None,
        direct: bool = None,
    ) -> "Stream":
        """Manipulate video frame metadata."""
        return self._apply_filter(
            filter_name="metadata",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "key": key,
                "value": value,
                "function": function,
                "expr": expr,
                "file": file,
                "direct": direct,
            },
        )[0]

    def midequalizer(self, in1_stream: "Stream", planes: int = None) -> "Stream":
        """Apply Midway Equalization."""
        return self._apply_filter(
            filter_name="midequalizer",
            inputs=[self, in1_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def minterpolate(
        self,
        fps: str = None,
        mi_mode: Literal["dup", "blend", "mci"] | int = None,
        mc_mode: Literal["obmc", "aobmc"] | int = None,
        me_mode: Literal["bidir", "bilat"] | int = None,
        me: Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"]
        | int = None,
        mb_size: int = None,
        search_param: int = None,
        vsbmc: int = None,
        scd: Literal["none", "fdiff"] | int = None,
        scd_threshold: float = None,
    ) -> "Stream":
        """Frame rate conversion using Motion Interpolation."""
        return self._apply_filter(
            filter_name="minterpolate",
            inputs=[self],
            named_arguments={
                "fps": fps,
                "mi_mode": mi_mode,
                "mc_mode": mc_mode,
                "me_mode": me_mode,
                "me": me,
                "mb_size": mb_size,
                "search_param": search_param,
                "vsbmc": vsbmc,
                "scd": scd,
                "scd_threshold": scd_threshold,
            },
        )[0]

    def mix(
        self,
        *streams: "Stream",
        inputs: int = None,
        weights: str = None,
        scale: float = None,
        planes: str = None,
        duration: Literal["longest", "shortest", "first"] | int = None,
    ) -> "Stream":
        """Mix video inputs."""
        return self._apply_filter(
            filter_name="mix",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "weights": weights,
                "scale": scale,
                "planes": planes,
                "duration": duration,
            },
        )[0]

    def monochrome(
        self, cb: float = None, cr: float = None, size: float = None, high: float = None
    ) -> "Stream":
        """Convert video to gray using custom color filter."""
        return self._apply_filter(
            filter_name="monochrome",
            inputs=[self],
            named_arguments={
                "cb": cb,
                "cr": cr,
                "size": size,
                "high": high,
            },
        )[0]

    def morpho(
        self,
        structure_stream: "Stream",
        mode: Literal[
            "erode", "dilate", "open", "close", "gradient", "tophat", "blackhat"
        ]
        | int = None,
        planes: int = None,
        structure: Literal["first", "all"] | int = None,
    ) -> "Stream":
        """Apply Morphological filter."""
        return self._apply_filter(
            filter_name="morpho",
            inputs=[self, structure_stream],
            named_arguments={
                "mode": mode,
                "planes": planes,
                "structure": structure,
            },
        )[0]

    def mpdecimate(
        self,
        max: int = None,
        keep: int = None,
        hi: int = None,
        lo: int = None,
        frac: float = None,
    ) -> "Stream":
        """Remove near-duplicate frames."""
        return self._apply_filter(
            filter_name="mpdecimate",
            inputs=[self],
            named_arguments={
                "max": max,
                "keep": keep,
                "hi": hi,
                "lo": lo,
                "frac": frac,
            },
        )[0]

    def msad(self, reference_stream: "Stream") -> "Stream":
        """Calculate the MSAD between two video streams."""
        return self._apply_filter(
            filter_name="msad", inputs=[self, reference_stream], named_arguments={}
        )[0]

    def multiply(
        self,
        factor_stream: "Stream",
        scale: float = None,
        offset: float = None,
        planes: str = None,
    ) -> "Stream":
        """Multiply first video stream with second video stream."""
        return self._apply_filter(
            filter_name="multiply",
            inputs=[self, factor_stream],
            named_arguments={
                "scale": scale,
                "offset": offset,
                "planes": planes,
            },
        )[0]

    def negate(
        self,
        components: Literal["y", "u", "v", "r", "g", "b", "a"] = None,
        negate_alpha: bool = None,
    ) -> "Stream":
        """Negate input video."""
        return self._apply_filter(
            filter_name="negate",
            inputs=[self],
            named_arguments={
                "components": components,
                "negate_alpha": negate_alpha,
            },
        )[0]

    def nlmeans(
        self,
        s: float = None,
        p: int = None,
        pc: int = None,
        r: int = None,
        rc: int = None,
    ) -> "Stream":
        """Non-local means denoiser."""
        return self._apply_filter(
            filter_name="nlmeans",
            inputs=[self],
            named_arguments={
                "s": s,
                "p": p,
                "pc": pc,
                "r": r,
                "rc": rc,
            },
        )[0]

    def nnedi(
        self,
        weights: str = None,
        deint: Literal["all", "interlaced"] | int = None,
        field: Literal["af", "a", "t", "b", "tf", "bf"] | int = None,
        planes: int = None,
        nsize: Literal["s8x6", "s16x6", "s32x6", "s48x6", "s8x4", "s16x4", "s32x4"]
        | int = None,
        nns: Literal["n16", "n32", "n64", "n128", "n256"] | int = None,
        qual: Literal["fast", "slow"] | int = None,
        etype: Literal["a", "abs", "s", "mse"] | int = None,
        pscrn: Literal["none", "original", "new", "new2", "new3"] | int = None,
    ) -> "Stream":
        """Apply neural network edge directed interpolation intra-only deinterlacer."""
        return self._apply_filter(
            filter_name="nnedi",
            inputs=[self],
            named_arguments={
                "weights": weights,
                "deint": deint,
                "field": field,
                "planes": planes,
                "nsize": nsize,
                "nns": nns,
                "qual": qual,
                "etype": etype,
                "pscrn": pscrn,
            },
        )[0]

    def noformat(
        self, pix_fmts: str = None, color_spaces: str = None, color_ranges: str = None
    ) -> "Stream":
        """Force libavfilter not to use any of the specified pixel formats for the input to the next filter."""
        return self._apply_filter(
            filter_name="noformat",
            inputs=[self],
            named_arguments={
                "pix_fmts": pix_fmts,
                "color_spaces": color_spaces,
                "color_ranges": color_ranges,
            },
        )[0]

    def noise(
        self,
        all_seed: int = None,
        all_strength: int = None,
        alls: int = None,
        all_flags: Literal["a", "p", "t", "u"] = None,
        allf: Literal["a", "p", "t", "u"] = None,
        c0_seed: int = None,
        c0_strength: int = None,
        c0s: int = None,
        c0_flags: Literal["a", "p", "t", "u"] = None,
        c0f: Literal["a", "p", "t", "u"] = None,
        c1_seed: int = None,
        c1_strength: int = None,
        c1s: int = None,
        c1_flags: Literal["a", "p", "t", "u"] = None,
        c1f: Literal["a", "p", "t", "u"] = None,
        c2_seed: int = None,
        c2_strength: int = None,
        c2s: int = None,
        c2_flags: Literal["a", "p", "t", "u"] = None,
        c2f: Literal["a", "p", "t", "u"] = None,
        c3_seed: int = None,
        c3_strength: int = None,
        c3s: int = None,
        c3_flags: Literal["a", "p", "t", "u"] = None,
        c3f: Literal["a", "p", "t", "u"] = None,
    ) -> "Stream":
        """Add noise."""
        return self._apply_filter(
            filter_name="noise",
            inputs=[self],
            named_arguments={
                "all_seed": all_seed,
                "all_strength": all_strength,
                "alls": alls,
                "all_flags": all_flags,
                "allf": allf,
                "c0_seed": c0_seed,
                "c0_strength": c0_strength,
                "c0s": c0s,
                "c0_flags": c0_flags,
                "c0f": c0f,
                "c1_seed": c1_seed,
                "c1_strength": c1_strength,
                "c1s": c1s,
                "c1_flags": c1_flags,
                "c1f": c1f,
                "c2_seed": c2_seed,
                "c2_strength": c2_strength,
                "c2s": c2s,
                "c2_flags": c2_flags,
                "c2f": c2f,
                "c3_seed": c3_seed,
                "c3_strength": c3_strength,
                "c3s": c3s,
                "c3_flags": c3_flags,
                "c3f": c3f,
            },
        )[0]

    def normalize(
        self,
        blackpt: str = None,
        whitept: str = None,
        smoothing: int = None,
        independence: float = None,
        strength: float = None,
    ) -> "Stream":
        """Normalize RGB video."""
        return self._apply_filter(
            filter_name="normalize",
            inputs=[self],
            named_arguments={
                "blackpt": blackpt,
                "whitept": whitept,
                "smoothing": smoothing,
                "independence": independence,
                "strength": strength,
            },
        )[0]

    def null(self) -> "Stream":
        """Pass the source unchanged to the output."""
        return self._apply_filter(
            filter_name="null", inputs=[self], named_arguments={}
        )[0]

    def ocr(
        self,
        datapath: str = None,
        language: str = None,
        whitelist: str = None,
        blacklist: str = None,
    ) -> "Stream":
        """Optical Character Recognition."""
        return self._apply_filter(
            filter_name="ocr",
            inputs=[self],
            named_arguments={
                "datapath": datapath,
                "language": language,
                "whitelist": whitelist,
                "blacklist": blacklist,
            },
        )[0]

    def oscilloscope(
        self,
        x: float = None,
        y: float = None,
        s: float = None,
        t: float = None,
        o: float = None,
        tx: float = None,
        ty: float = None,
        tw: float = None,
        th: float = None,
        c: int = None,
        g: bool = None,
        st: bool = None,
        sc: bool = None,
    ) -> "Stream":
        """2D Video Oscilloscope."""
        return self._apply_filter(
            filter_name="oscilloscope",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "s": s,
                "t": t,
                "o": o,
                "tx": tx,
                "ty": ty,
                "tw": tw,
                "th": th,
                "c": c,
                "g": g,
                "st": st,
                "sc": sc,
            },
        )[0]

    def overlay(
        self,
        overlay_stream: "Stream",
        x: str = None,
        y: str = None,
        eof_action: Literal["repeat", "endall", "pass"] | int = None,
        eval: Literal["init", "frame"] | int = None,
        shortest: bool = None,
        format: Literal[
            "yuv420",
            "yuv420p10",
            "yuv422",
            "yuv422p10",
            "yuv444",
            "yuv444p10",
            "rgb",
            "gbrp",
            "auto",
        ]
        | int = None,
        repeatlast: bool = None,
        alpha: Literal["straight", "premultiplied"] | int = None,
    ) -> "Stream":
        """Overlay a video source on top of the input."""
        return self._apply_filter(
            filter_name="overlay",
            inputs=[self, overlay_stream],
            named_arguments={
                "x": x,
                "y": y,
                "eof_action": eof_action,
                "eval": eval,
                "shortest": shortest,
                "format": format,
                "repeatlast": repeatlast,
                "alpha": alpha,
            },
        )[0]

    def owdenoise(
        self,
        depth: int = None,
        luma_strength: float = None,
        ls: float = None,
        chroma_strength: float = None,
        cs: float = None,
    ) -> "Stream":
        """Denoise using wavelets."""
        return self._apply_filter(
            filter_name="owdenoise",
            inputs=[self],
            named_arguments={
                "depth": depth,
                "luma_strength": luma_strength,
                "ls": ls,
                "chroma_strength": chroma_strength,
                "cs": cs,
            },
        )[0]

    def pad(
        self,
        width: str = None,
        w: str = None,
        height: str = None,
        h: str = None,
        x: str = None,
        y: str = None,
        color: str = None,
        eval: Literal["init", "frame"] | int = None,
        aspect: str = None,
    ) -> "Stream":
        """Pad the input video."""
        return self._apply_filter(
            filter_name="pad",
            inputs=[self],
            named_arguments={
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "x": x,
                "y": y,
                "color": color,
                "eval": eval,
                "aspect": aspect,
            },
        )[0]

    def palettegen(
        self,
        max_colors: int = None,
        reserve_transparent: bool = None,
        transparency_color: str = None,
        stats_mode: Literal["full", "diff", "single"] | int = None,
    ) -> "Stream":
        """Find the optimal palette for a given stream."""
        return self._apply_filter(
            filter_name="palettegen",
            inputs=[self],
            named_arguments={
                "max_colors": max_colors,
                "reserve_transparent": reserve_transparent,
                "transparency_color": transparency_color,
                "stats_mode": stats_mode,
            },
        )[0]

    def paletteuse(
        self,
        palette_stream: "Stream",
        dither: Literal[
            "bayer",
            "heckbert",
            "floyd_steinberg",
            "sierra2",
            "sierra2_4a",
            "sierra3",
            "burkes",
            "atkinson",
        ]
        | int = None,
        bayer_scale: int = None,
        diff_mode: Literal["rectangle"] | int = None,
        new: bool = None,
        alpha_threshold: int = None,
        debug_kdtree: str = None,
    ) -> "Stream":
        """Use a palette to downsample an input video stream."""
        return self._apply_filter(
            filter_name="paletteuse",
            inputs=[self, palette_stream],
            named_arguments={
                "dither": dither,
                "bayer_scale": bayer_scale,
                "diff_mode": diff_mode,
                "new": new,
                "alpha_threshold": alpha_threshold,
                "debug_kdtree": debug_kdtree,
            },
        )[0]

    def pan(self, args: str = None) -> "Stream":
        """Remix channels with coefficients (panning)."""
        return self._apply_filter(
            filter_name="pan",
            inputs=[self],
            named_arguments={
                "args": args,
            },
        )[0]

    def perms(
        self,
        mode: Literal["none", "ro", "rw", "toggle", "random"] | int = None,
        seed: str = None,
    ) -> "Stream":
        """Set permissions for the output video frame."""
        return self._apply_filter(
            filter_name="perms",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "seed": seed,
            },
        )[0]

    def perspective(
        self,
        x0: str = None,
        y0: str = None,
        x1: str = None,
        y1: str = None,
        x2: str = None,
        y2: str = None,
        x3: str = None,
        y3: str = None,
        interpolation: Literal["linear", "cubic"] | int = None,
        sense: Literal["source", "destination"] | int = None,
        eval: Literal["init", "frame"] | int = None,
    ) -> "Stream":
        """Correct the perspective of video."""
        return self._apply_filter(
            filter_name="perspective",
            inputs=[self],
            named_arguments={
                "x0": x0,
                "y0": y0,
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "x3": x3,
                "y3": y3,
                "interpolation": interpolation,
                "sense": sense,
                "eval": eval,
            },
        )[0]

    def phase(
        self, mode: Literal["p", "t", "b", "T", "B", "u", "U", "a", "A"] | int = None
    ) -> "Stream":
        """Phase shift fields."""
        return self._apply_filter(
            filter_name="phase",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def photosensitivity(
        self,
        frames: int = None,
        f: int = None,
        threshold: float = None,
        t: float = None,
        skip: int = None,
        bypass: bool = None,
    ) -> "Stream":
        """Filter out photosensitive epilepsy seizure-inducing flashes."""
        return self._apply_filter(
            filter_name="photosensitivity",
            inputs=[self],
            named_arguments={
                "frames": frames,
                "f": f,
                "threshold": threshold,
                "t": t,
                "skip": skip,
                "bypass": bypass,
            },
        )[0]

    def pixdesctest(self) -> "Stream":
        """Test pixel format definitions."""
        return self._apply_filter(
            filter_name="pixdesctest", inputs=[self], named_arguments={}
        )[0]

    def pixelize(
        self,
        width: int = None,
        w: int = None,
        height: int = None,
        h: int = None,
        mode: Literal["avg", "min", "max"] | int = None,
        m: Literal["avg", "min", "max"] | int = None,
        planes: str = None,
        p: str = None,
    ) -> "Stream":
        """Pixelize video."""
        return self._apply_filter(
            filter_name="pixelize",
            inputs=[self],
            named_arguments={
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "mode": mode,
                "m": m,
                "planes": planes,
                "p": p,
            },
        )[0]

    def pixscope(
        self,
        x: float = None,
        y: float = None,
        w: int = None,
        h: int = None,
        o: float = None,
        wx: float = None,
        wy: float = None,
    ) -> "Stream":
        """Pixel data analysis."""
        return self._apply_filter(
            filter_name="pixscope",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "o": o,
                "wx": wx,
                "wy": wy,
            },
        )[0]

    def pp7(
        self, qp: int = None, mode: Literal["hard", "soft", "medium"] | int = None
    ) -> "Stream":
        """Apply Postprocessing 7 filter."""
        return self._apply_filter(
            filter_name="pp7",
            inputs=[self],
            named_arguments={
                "qp": qp,
                "mode": mode,
            },
        )[0]

    def premultiply(
        self, *streams: "Stream", planes: int = None, inplace: bool = None
    ) -> "Stream":
        """PreMultiply first stream with first plane of second stream."""
        return self._apply_filter(
            filter_name="premultiply",
            inputs=[self, *streams],
            named_arguments={
                "planes": planes,
                "inplace": inplace,
            },
        )[0]

    def prewitt(
        self, planes: int = None, scale: float = None, delta: float = None
    ) -> "Stream":
        """Apply prewitt operator."""
        return self._apply_filter(
            filter_name="prewitt",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def pseudocolor(
        self,
        c0: str = None,
        c1: str = None,
        c2: str = None,
        c3: str = None,
        index: int = None,
        i: int = None,
        preset: Literal[
            "none",
            "magma",
            "inferno",
            "plasma",
            "viridis",
            "turbo",
            "cividis",
            "range1",
            "range2",
            "shadows",
            "highlights",
            "solar",
            "nominal",
            "preferred",
            "total",
            "spectral",
            "cool",
            "heat",
            "fiery",
            "blues",
            "green",
            "helix",
        ]
        | int = None,
        p: Literal[
            "none",
            "magma",
            "inferno",
            "plasma",
            "viridis",
            "turbo",
            "cividis",
            "range1",
            "range2",
            "shadows",
            "highlights",
            "solar",
            "nominal",
            "preferred",
            "total",
            "spectral",
            "cool",
            "heat",
            "fiery",
            "blues",
            "green",
            "helix",
        ]
        | int = None,
        opacity: float = None,
    ) -> "Stream":
        """Make pseudocolored video frames."""
        return self._apply_filter(
            filter_name="pseudocolor",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "index": index,
                "i": i,
                "preset": preset,
                "p": p,
                "opacity": opacity,
            },
        )[0]

    def psnr(
        self,
        reference_stream: "Stream",
        stats_file: str = None,
        f: str = None,
        stats_version: int = None,
        output_max: bool = None,
    ) -> "Stream":
        """Calculate the PSNR between two video streams."""
        return self._apply_filter(
            filter_name="psnr",
            inputs=[self, reference_stream],
            named_arguments={
                "stats_file": stats_file,
                "f": f,
                "stats_version": stats_version,
                "output_max": output_max,
            },
        )[0]

    def pullup(
        self,
        jl: int = None,
        jr: int = None,
        jt: int = None,
        jb: int = None,
        sb: bool = None,
        mp: Literal["y", "u", "v"] | int = None,
    ) -> "Stream":
        """Pullup from field sequence to frames."""
        return self._apply_filter(
            filter_name="pullup",
            inputs=[self],
            named_arguments={
                "jl": jl,
                "jr": jr,
                "jt": jt,
                "jb": jb,
                "sb": sb,
                "mp": mp,
            },
        )[0]

    def qp(self, qp: str = None) -> "Stream":
        """Change video quantization parameters."""
        return self._apply_filter(
            filter_name="qp",
            inputs=[self],
            named_arguments={
                "qp": qp,
            },
        )[0]

    def random(self, frames: int = None, seed: str = None) -> "Stream":
        """Return random frames."""
        return self._apply_filter(
            filter_name="random",
            inputs=[self],
            named_arguments={
                "frames": frames,
                "seed": seed,
            },
        )[0]

    def readeia608(
        self,
        scan_min: int = None,
        scan_max: int = None,
        spw: float = None,
        chp: bool = None,
        lp: bool = None,
    ) -> "Stream":
        """Read EIA-608 Closed Caption codes from input video and write them to frame metadata."""
        return self._apply_filter(
            filter_name="readeia608",
            inputs=[self],
            named_arguments={
                "scan_min": scan_min,
                "scan_max": scan_max,
                "spw": spw,
                "chp": chp,
                "lp": lp,
            },
        )[0]

    def readvitc(
        self, scan_max: int = None, thr_b: float = None, thr_w: float = None
    ) -> "Stream":
        """Read vertical interval timecode and write it to frame metadata."""
        return self._apply_filter(
            filter_name="readvitc",
            inputs=[self],
            named_arguments={
                "scan_max": scan_max,
                "thr_b": thr_b,
                "thr_w": thr_w,
            },
        )[0]

    def realtime(self, limit: str = None, speed: float = None) -> "Stream":
        """Slow down filtering to match realtime."""
        return self._apply_filter(
            filter_name="realtime",
            inputs=[self],
            named_arguments={
                "limit": limit,
                "speed": speed,
            },
        )[0]

    def remap(
        self,
        xmap_stream: "Stream",
        ymap_stream: "Stream",
        format: Literal["color", "gray"] | int = None,
        fill: str = None,
    ) -> "Stream":
        """Remap pixels."""
        return self._apply_filter(
            filter_name="remap",
            inputs=[self, xmap_stream, ymap_stream],
            named_arguments={
                "format": format,
                "fill": fill,
            },
        )[0]

    def removegrain(
        self, m0: int = None, m1: int = None, m2: int = None, m3: int = None
    ) -> "Stream":
        """Remove grain."""
        return self._apply_filter(
            filter_name="removegrain",
            inputs=[self],
            named_arguments={
                "m0": m0,
                "m1": m1,
                "m2": m2,
                "m3": m3,
            },
        )[0]

    def removelogo(self, filename: str = None, f: str = None) -> "Stream":
        """Remove a TV logo based on a mask image."""
        return self._apply_filter(
            filter_name="removelogo",
            inputs=[self],
            named_arguments={
                "filename": filename,
                "f": f,
            },
        )[0]

    def repeatfields(self) -> "Stream":
        """Hard repeat fields based on MPEG repeat field flag."""
        return self._apply_filter(
            filter_name="repeatfields", inputs=[self], named_arguments={}
        )[0]

    def replaygain(
        self, track_gain: float = None, track_peak: float = None
    ) -> "Stream":
        """ReplayGain scanner."""
        return self._apply_filter(
            filter_name="replaygain",
            inputs=[self],
            named_arguments={
                "track_gain": track_gain,
                "track_peak": track_peak,
            },
        )[0]

    def reverse(self) -> "Stream":
        """Reverse a clip."""
        return self._apply_filter(
            filter_name="reverse", inputs=[self], named_arguments={}
        )[0]

    def rgbashift(
        self,
        rh: int = None,
        rv: int = None,
        gh: int = None,
        gv: int = None,
        bh: int = None,
        bv: int = None,
        ah: int = None,
        av: int = None,
        edge: Literal["smear", "wrap"] | int = None,
    ) -> "Stream":
        """Shift RGBA."""
        return self._apply_filter(
            filter_name="rgbashift",
            inputs=[self],
            named_arguments={
                "rh": rh,
                "rv": rv,
                "gh": gh,
                "gv": gv,
                "bh": bh,
                "bv": bv,
                "ah": ah,
                "av": av,
                "edge": edge,
            },
        )[0]

    def roberts(
        self, planes: int = None, scale: float = None, delta: float = None
    ) -> "Stream":
        """Apply roberts cross operator."""
        return self._apply_filter(
            filter_name="roberts",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def rotate(
        self,
        angle: str = None,
        a: str = None,
        out_w: str = None,
        ow: str = None,
        out_h: str = None,
        oh: str = None,
        fillcolor: str = None,
        c: str = None,
        bilinear: bool = None,
    ) -> "Stream":
        """Rotate the input image."""
        return self._apply_filter(
            filter_name="rotate",
            inputs=[self],
            named_arguments={
                "angle": angle,
                "a": a,
                "out_w": out_w,
                "ow": ow,
                "out_h": out_h,
                "oh": oh,
                "fillcolor": fillcolor,
                "c": c,
                "bilinear": bilinear,
            },
        )[0]

    def rubberband(
        self,
        tempo: float = None,
        pitch: float = None,
        transients: Literal["crisp", "mixed", "smooth"] | int = None,
        detector: Literal["compound", "percussive", "soft"] | int = None,
        phase: Literal["laminar", "independent"] | int = None,
        window: Literal["standard", "short", "long"] | int = None,
        smoothing: Literal["off", "on"] | int = None,
        formant: Literal["shifted", "preserved"] | int = None,
        pitchq: Literal["quality", "speed", "consistency"] | int = None,
        channels: Literal["apart", "together"] | int = None,
    ) -> "Stream":
        """Apply time-stretching and pitch-shifting."""
        return self._apply_filter(
            filter_name="rubberband",
            inputs=[self],
            named_arguments={
                "tempo": tempo,
                "pitch": pitch,
                "transients": transients,
                "detector": detector,
                "phase": phase,
                "window": window,
                "smoothing": smoothing,
                "formant": formant,
                "pitchq": pitchq,
                "channels": channels,
            },
        )[0]

    def sab(
        self,
        luma_radius: float = None,
        lr: float = None,
        luma_pre_filter_radius: float = None,
        lpfr: float = None,
        luma_strength: float = None,
        ls: float = None,
        chroma_radius: float = None,
        cr: float = None,
        chroma_pre_filter_radius: float = None,
        cpfr: float = None,
        chroma_strength: float = None,
        cs: float = None,
    ) -> "Stream":
        """Apply shape adaptive blur."""
        return self._apply_filter(
            filter_name="sab",
            inputs=[self],
            named_arguments={
                "luma_radius": luma_radius,
                "lr": lr,
                "luma_pre_filter_radius": luma_pre_filter_radius,
                "lpfr": lpfr,
                "luma_strength": luma_strength,
                "ls": ls,
                "chroma_radius": chroma_radius,
                "cr": cr,
                "chroma_pre_filter_radius": chroma_pre_filter_radius,
                "cpfr": cpfr,
                "chroma_strength": chroma_strength,
                "cs": cs,
            },
        )[0]

    def scale(
        self,
        w: str = None,
        width: str = None,
        h: str = None,
        height: str = None,
        flags: str = None,
        interl: bool = None,
        size: str = None,
        s: str = None,
        in_color_matrix: Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | int = None,
        out_color_matrix: Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | int = None,
        in_range: Literal[
            "auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"
        ]
        | int = None,
        out_range: Literal[
            "auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"
        ]
        | int = None,
        in_chroma_loc: Literal[
            "auto",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int = None,
        out_chroma_loc: Literal[
            "auto",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int = None,
        in_primaries: Literal[
            "auto",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        out_primaries: Literal[
            "auto",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        in_transfer: Literal[
            "auto",
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "iec61966-2-1",
            "srgb",
            "iec61966-2-4",
            "xvycc",
            "bt1361e",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int = None,
        out_transfer: Literal[
            "auto",
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "iec61966-2-1",
            "srgb",
            "iec61966-2-4",
            "xvycc",
            "bt1361e",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int = None,
        in_v_chr_pos: int = None,
        in_h_chr_pos: int = None,
        out_v_chr_pos: int = None,
        out_h_chr_pos: int = None,
        force_original_aspect_ratio: Literal["disable", "decrease", "increase"]
        | int = None,
        force_divisible_by: int = None,
        reset_sar: bool = None,
        param0: float = None,
        param1: float = None,
        eval: Literal["init", "frame"] | int = None,
    ) -> "Stream":
        """Scale the input video size and/or convert the image format."""
        return self._apply_filter(
            filter_name="scale",
            inputs=[self],
            named_arguments={
                "w": w,
                "width": width,
                "h": h,
                "height": height,
                "flags": flags,
                "interl": interl,
                "size": size,
                "s": s,
                "in_color_matrix": in_color_matrix,
                "out_color_matrix": out_color_matrix,
                "in_range": in_range,
                "out_range": out_range,
                "in_chroma_loc": in_chroma_loc,
                "out_chroma_loc": out_chroma_loc,
                "in_primaries": in_primaries,
                "out_primaries": out_primaries,
                "in_transfer": in_transfer,
                "out_transfer": out_transfer,
                "in_v_chr_pos": in_v_chr_pos,
                "in_h_chr_pos": in_h_chr_pos,
                "out_v_chr_pos": out_v_chr_pos,
                "out_h_chr_pos": out_h_chr_pos,
                "force_original_aspect_ratio": force_original_aspect_ratio,
                "force_divisible_by": force_divisible_by,
                "reset_sar": reset_sar,
                "param0": param0,
                "param1": param1,
                "eval": eval,
            },
        )[0]

    def scale2ref(
        self,
        ref_stream: "Stream",
        w: str = None,
        width: str = None,
        h: str = None,
        height: str = None,
        flags: str = None,
        interl: bool = None,
        size: str = None,
        s: str = None,
        in_color_matrix: Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | int = None,
        out_color_matrix: Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | int = None,
        in_range: Literal[
            "auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"
        ]
        | int = None,
        out_range: Literal[
            "auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"
        ]
        | int = None,
        in_chroma_loc: Literal[
            "auto",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int = None,
        out_chroma_loc: Literal[
            "auto",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int = None,
        in_primaries: Literal[
            "auto",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        out_primaries: Literal[
            "auto",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        in_transfer: Literal[
            "auto",
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "iec61966-2-1",
            "srgb",
            "iec61966-2-4",
            "xvycc",
            "bt1361e",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int = None,
        out_transfer: Literal[
            "auto",
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "iec61966-2-1",
            "srgb",
            "iec61966-2-4",
            "xvycc",
            "bt1361e",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int = None,
        in_v_chr_pos: int = None,
        in_h_chr_pos: int = None,
        out_v_chr_pos: int = None,
        out_h_chr_pos: int = None,
        force_original_aspect_ratio: Literal["disable", "decrease", "increase"]
        | int = None,
        force_divisible_by: int = None,
        reset_sar: bool = None,
        param0: float = None,
        param1: float = None,
        eval: Literal["init", "frame"] | int = None,
    ) -> list["Stream"]:
        """Scale the input video size and/or convert the image format to the given reference."""
        return self._apply_filter(
            filter_name="scale2ref",
            inputs=[self, ref_stream],
            named_arguments={
                "w": w,
                "width": width,
                "h": h,
                "height": height,
                "flags": flags,
                "interl": interl,
                "size": size,
                "s": s,
                "in_color_matrix": in_color_matrix,
                "out_color_matrix": out_color_matrix,
                "in_range": in_range,
                "out_range": out_range,
                "in_chroma_loc": in_chroma_loc,
                "out_chroma_loc": out_chroma_loc,
                "in_primaries": in_primaries,
                "out_primaries": out_primaries,
                "in_transfer": in_transfer,
                "out_transfer": out_transfer,
                "in_v_chr_pos": in_v_chr_pos,
                "in_h_chr_pos": in_h_chr_pos,
                "out_v_chr_pos": out_v_chr_pos,
                "out_h_chr_pos": out_h_chr_pos,
                "force_original_aspect_ratio": force_original_aspect_ratio,
                "force_divisible_by": force_divisible_by,
                "reset_sar": reset_sar,
                "param0": param0,
                "param1": param1,
                "eval": eval,
            },
            num_output_streams=2,
        )

    def scale_vt(
        self,
        w: str = None,
        h: str = None,
        color_matrix: str = None,
        color_primaries: str = None,
        color_transfer: str = None,
    ) -> "Stream":
        """Scale Videotoolbox frames"""
        return self._apply_filter(
            filter_name="scale_vt",
            inputs=[self],
            named_arguments={
                "w": w,
                "h": h,
                "color_matrix": color_matrix,
                "color_primaries": color_primaries,
                "color_transfer": color_transfer,
            },
        )[0]

    def scdet(
        self,
        threshold: float = None,
        t: float = None,
        sc_pass: bool = None,
        s: bool = None,
    ) -> "Stream":
        """Detect video scene change"""
        return self._apply_filter(
            filter_name="scdet",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "t": t,
                "sc_pass": sc_pass,
                "s": s,
            },
        )[0]

    def scharr(
        self, planes: int = None, scale: float = None, delta: float = None
    ) -> "Stream":
        """Apply scharr operator."""
        return self._apply_filter(
            filter_name="scharr",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def scroll(
        self,
        horizontal: float = None,
        h: float = None,
        vertical: float = None,
        v: float = None,
        hpos: float = None,
        vpos: float = None,
    ) -> "Stream":
        """Scroll input video."""
        return self._apply_filter(
            filter_name="scroll",
            inputs=[self],
            named_arguments={
                "horizontal": horizontal,
                "h": h,
                "vertical": vertical,
                "v": v,
                "hpos": hpos,
                "vpos": vpos,
            },
        )[0]

    def segment(
        self, timestamps: str = None, frames: str = None
    ) -> "FilterMultiOutput":
        """Segment video stream."""
        return self._apply_dynamic_outputs_filter(
            filter_name="segment",
            inputs=[self],
            named_arguments={
                "timestamps": timestamps,
                "frames": frames,
            },
        )

    def select(
        self, expr: str = None, e: str = None, outputs: int = None, n: int = None
    ) -> "FilterMultiOutput":
        """Select video frames to pass in output."""
        return self._apply_dynamic_outputs_filter(
            filter_name="select",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "e": e,
                "outputs": outputs,
                "n": n,
            },
        )

    def selectivecolor(
        self,
        correction_method: Literal["absolute", "relative"] | int = None,
        reds: str = None,
        yellows: str = None,
        greens: str = None,
        cyans: str = None,
        blues: str = None,
        magentas: str = None,
        whites: str = None,
        neutrals: str = None,
        blacks: str = None,
        psfile: str = None,
    ) -> "Stream":
        """Apply CMYK adjustments to specific color ranges."""
        return self._apply_filter(
            filter_name="selectivecolor",
            inputs=[self],
            named_arguments={
                "correction_method": correction_method,
                "reds": reds,
                "yellows": yellows,
                "greens": greens,
                "cyans": cyans,
                "blues": blues,
                "magentas": magentas,
                "whites": whites,
                "neutrals": neutrals,
                "blacks": blacks,
                "psfile": psfile,
            },
        )[0]

    def sendcmd(
        self, commands: str = None, c: str = None, filename: str = None, f: str = None
    ) -> "Stream":
        """Send commands to filters."""
        return self._apply_filter(
            filter_name="sendcmd",
            inputs=[self],
            named_arguments={
                "commands": commands,
                "c": c,
                "filename": filename,
                "f": f,
            },
        )[0]

    def separatefields(self) -> "Stream":
        """Split input video frames into fields."""
        return self._apply_filter(
            filter_name="separatefields", inputs=[self], named_arguments={}
        )[0]

    def setdar(
        self, dar: str = None, ratio: str = None, r: str = None, max: int = None
    ) -> "Stream":
        """Set the frame display aspect ratio."""
        return self._apply_filter(
            filter_name="setdar",
            inputs=[self],
            named_arguments={
                "dar": dar,
                "ratio": ratio,
                "r": r,
                "max": max,
            },
        )[0]

    def setfield(
        self, mode: Literal["auto", "bff", "tff", "prog"] | int = None
    ) -> "Stream":
        """Force field for the output video frame."""
        return self._apply_filter(
            filter_name="setfield",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def setparams(
        self,
        field_mode: Literal["auto", "bff", "tff", "prog"] | int = None,
        range: Literal[
            "auto",
            "unspecified",
            "unknown",
            "limited",
            "tv",
            "mpeg",
            "full",
            "pc",
            "jpeg",
        ]
        | int = None,
        color_primaries: Literal[
            "auto",
            "bt709",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        color_trc: Literal[
            "auto",
            "bt709",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "linear",
            "log100",
            "log316",
            "iec61966-2-4",
            "bt1361e",
            "iec61966-2-1",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int = None,
        colorspace: Literal[
            "auto",
            "gbr",
            "bt709",
            "unknown",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "ycgco-re",
            "ycgco-ro",
            "bt2020nc",
            "bt2020c",
            "smpte2085",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
            "ipt-c2",
        ]
        | int = None,
        chroma_location: Literal[
            "auto",
            "unspecified",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int = None,
    ) -> "Stream":
        """Force field, or color property for the output video frame."""
        return self._apply_filter(
            filter_name="setparams",
            inputs=[self],
            named_arguments={
                "field_mode": field_mode,
                "range": range,
                "color_primaries": color_primaries,
                "color_trc": color_trc,
                "colorspace": colorspace,
                "chroma_location": chroma_location,
            },
        )[0]

    def setpts(self, expr: str = None, strip_fps: bool = None) -> "Stream":
        """Set PTS for the output video frame."""
        return self._apply_filter(
            filter_name="setpts",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "strip_fps": strip_fps,
            },
        )[0]

    def setrange(
        self,
        range: Literal[
            "auto",
            "unspecified",
            "unknown",
            "limited",
            "tv",
            "mpeg",
            "full",
            "pc",
            "jpeg",
        ]
        | int = None,
    ) -> "Stream":
        """Force color range for the output video frame."""
        return self._apply_filter(
            filter_name="setrange",
            inputs=[self],
            named_arguments={
                "range": range,
            },
        )[0]

    def setsar(
        self, sar: str = None, ratio: str = None, r: str = None, max: int = None
    ) -> "Stream":
        """Set the pixel sample aspect ratio."""
        return self._apply_filter(
            filter_name="setsar",
            inputs=[self],
            named_arguments={
                "sar": sar,
                "ratio": ratio,
                "r": r,
                "max": max,
            },
        )[0]

    def settb(self, expr: str = None, tb: str = None) -> "Stream":
        """Set timebase for the video output link."""
        return self._apply_filter(
            filter_name="settb",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "tb": tb,
            },
        )[0]

    def shear(
        self,
        shx: float = None,
        shy: float = None,
        fillcolor: str = None,
        c: str = None,
        interp: Literal["nearest", "bilinear"] | int = None,
    ) -> "Stream":
        """Shear transform the input image."""
        return self._apply_filter(
            filter_name="shear",
            inputs=[self],
            named_arguments={
                "shx": shx,
                "shy": shy,
                "fillcolor": fillcolor,
                "c": c,
                "interp": interp,
            },
        )[0]

    def showcqt(
        self,
        size: str = None,
        s: str = None,
        fps: str = None,
        rate: str = None,
        r: str = None,
        bar_h: int = None,
        axis_h: int = None,
        sono_h: int = None,
        fullhd: bool = None,
        sono_v: str = None,
        volume: str = None,
        bar_v: str = None,
        volume2: str = None,
        sono_g: float = None,
        gamma: float = None,
        bar_g: float = None,
        gamma2: float = None,
        bar_t: float = None,
        timeclamp: float = None,
        tc: float = None,
        attack: float = None,
        basefreq: float = None,
        endfreq: float = None,
        coeffclamp: float = None,
        tlength: str = None,
        count: int = None,
        fcount: int = None,
        fontfile: str = None,
        font: str = None,
        fontcolor: str = None,
        axisfile: str = None,
        axis: bool = None,
        text: bool = None,
        csp: Literal[
            "unspecified",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020ncl",
        ]
        | int = None,
        cscheme: str = None,
    ) -> "Stream":
        """Convert input audio to a CQT (Constant/Clamped Q Transform) spectrum video output."""
        return self._apply_filter(
            filter_name="showcqt",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "fps": fps,
                "rate": rate,
                "r": r,
                "bar_h": bar_h,
                "axis_h": axis_h,
                "sono_h": sono_h,
                "fullhd": fullhd,
                "sono_v": sono_v,
                "volume": volume,
                "bar_v": bar_v,
                "volume2": volume2,
                "sono_g": sono_g,
                "gamma": gamma,
                "bar_g": bar_g,
                "gamma2": gamma2,
                "bar_t": bar_t,
                "timeclamp": timeclamp,
                "tc": tc,
                "attack": attack,
                "basefreq": basefreq,
                "endfreq": endfreq,
                "coeffclamp": coeffclamp,
                "tlength": tlength,
                "count": count,
                "fcount": fcount,
                "fontfile": fontfile,
                "font": font,
                "fontcolor": fontcolor,
                "axisfile": axisfile,
                "axis": axis,
                "text": text,
                "csp": csp,
                "cscheme": cscheme,
            },
        )[0]

    def showcwt(
        self,
        size: str = None,
        s: str = None,
        rate: str = None,
        r: str = None,
        scale: Literal[
            "linear", "log", "bark", "mel", "erbs", "sqrt", "cbrt", "qdrt", "fm"
        ]
        | int = None,
        iscale: Literal["linear", "log", "sqrt", "cbrt", "qdrt"] | int = None,
        min: float = None,
        max: float = None,
        imin: float = None,
        imax: float = None,
        logb: float = None,
        deviation: float = None,
        pps: int = None,
        mode: Literal["magnitude", "phase", "magphase", "channel", "stereo"]
        | int = None,
        slide: Literal["replace", "scroll", "frame"] | int = None,
        direction: Literal["lr", "rl", "ud", "du"] | int = None,
        bar: float = None,
        rotation: float = None,
    ) -> "Stream":
        """Convert input audio to a CWT (Continuous Wavelet Transform) spectrum video output."""
        return self._apply_filter(
            filter_name="showcwt",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "rate": rate,
                "r": r,
                "scale": scale,
                "iscale": iscale,
                "min": min,
                "max": max,
                "imin": imin,
                "imax": imax,
                "logb": logb,
                "deviation": deviation,
                "pps": pps,
                "mode": mode,
                "slide": slide,
                "direction": direction,
                "bar": bar,
                "rotation": rotation,
            },
        )[0]

    def showfreqs(
        self,
        size: str = None,
        s: str = None,
        rate: str = None,
        r: str = None,
        mode: Literal["line", "bar", "dot"] | int = None,
        ascale: Literal["lin", "sqrt", "cbrt", "log"] | int = None,
        fscale: Literal["lin", "log", "rlog"] | int = None,
        win_size: int = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
        overlap: float = None,
        averaging: int = None,
        colors: str = None,
        cmode: Literal["combined", "separate"] | int = None,
        minamp: float = None,
        data: Literal["magnitude", "phase", "delay"] | int = None,
        channels: str = None,
    ) -> "Stream":
        """Convert input audio to a frequencies video output."""
        return self._apply_filter(
            filter_name="showfreqs",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "rate": rate,
                "r": r,
                "mode": mode,
                "ascale": ascale,
                "fscale": fscale,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                "averaging": averaging,
                "colors": colors,
                "cmode": cmode,
                "minamp": minamp,
                "data": data,
                "channels": channels,
            },
        )[0]

    def showinfo(
        self, checksum: bool = None, udu_sei_as_ascii: bool = None
    ) -> "Stream":
        """Show textual information for each video frame."""
        return self._apply_filter(
            filter_name="showinfo",
            inputs=[self],
            named_arguments={
                "checksum": checksum,
                "udu_sei_as_ascii": udu_sei_as_ascii,
            },
        )[0]

    def showpalette(self, s: int = None) -> "Stream":
        """Display frame palette."""
        return self._apply_filter(
            filter_name="showpalette",
            inputs=[self],
            named_arguments={
                "s": s,
            },
        )[0]

    def showspatial(
        self,
        size: str = None,
        s: str = None,
        win_size: int = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
        rate: str = None,
        r: str = None,
    ) -> "Stream":
        """Convert input audio to a spatial video output."""
        return self._apply_filter(
            filter_name="showspatial",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "win_size": win_size,
                "win_func": win_func,
                "rate": rate,
                "r": r,
            },
        )[0]

    def showspectrum(
        self,
        size: str = None,
        s: str = None,
        slide: Literal["replace", "scroll", "fullframe", "rscroll", "lreplace"]
        | int = None,
        mode: Literal["combined", "separate"] | int = None,
        color: Literal[
            "channel",
            "intensity",
            "rainbow",
            "moreland",
            "nebulae",
            "fire",
            "fiery",
            "fruit",
            "cool",
            "magma",
            "green",
            "viridis",
            "plasma",
            "cividis",
            "terrain",
        ]
        | int = None,
        scale: Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"] | int = None,
        fscale: Literal["lin", "log"] | int = None,
        saturation: float = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
        orientation: Literal["vertical", "horizontal"] | int = None,
        overlap: float = None,
        gain: float = None,
        data: Literal["magnitude", "phase", "uphase"] | int = None,
        rotation: float = None,
        start: int = None,
        stop: int = None,
        fps: str = None,
        legend: bool = None,
        drange: float = None,
        limit: float = None,
        opacity: float = None,
    ) -> "Stream":
        """Convert input audio to a spectrum video output."""
        return self._apply_filter(
            filter_name="showspectrum",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "slide": slide,
                "mode": mode,
                "color": color,
                "scale": scale,
                "fscale": fscale,
                "saturation": saturation,
                "win_func": win_func,
                "orientation": orientation,
                "overlap": overlap,
                "gain": gain,
                "data": data,
                "rotation": rotation,
                "start": start,
                "stop": stop,
                "fps": fps,
                "legend": legend,
                "drange": drange,
                "limit": limit,
                "opacity": opacity,
            },
        )[0]

    def showspectrumpic(
        self,
        size: str = None,
        s: str = None,
        mode: Literal["combined", "separate"] | int = None,
        color: Literal[
            "channel",
            "intensity",
            "rainbow",
            "moreland",
            "nebulae",
            "fire",
            "fiery",
            "fruit",
            "cool",
            "magma",
            "green",
            "viridis",
            "plasma",
            "cividis",
            "terrain",
        ]
        | int = None,
        scale: Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"] | int = None,
        fscale: Literal["lin", "log"] | int = None,
        saturation: float = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
        orientation: Literal["vertical", "horizontal"] | int = None,
        gain: float = None,
        legend: bool = None,
        rotation: float = None,
        start: int = None,
        stop: int = None,
        drange: float = None,
        limit: float = None,
        opacity: float = None,
    ) -> "Stream":
        """Convert input audio to a spectrum video output single picture."""
        return self._apply_filter(
            filter_name="showspectrumpic",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "mode": mode,
                "color": color,
                "scale": scale,
                "fscale": fscale,
                "saturation": saturation,
                "win_func": win_func,
                "orientation": orientation,
                "gain": gain,
                "legend": legend,
                "rotation": rotation,
                "start": start,
                "stop": stop,
                "drange": drange,
                "limit": limit,
                "opacity": opacity,
            },
        )[0]

    def showvolume(
        self,
        rate: str = None,
        r: str = None,
        b: int = None,
        w: int = None,
        h: int = None,
        f: float = None,
        c: str = None,
        t: bool = None,
        v: bool = None,
        dm: float = None,
        dmc: str = None,
        o: Literal["h", "v"] | int = None,
        s: int = None,
        p: float = None,
        m: Literal["p", "r"] | int = None,
        ds: Literal["lin", "log"] | int = None,
    ) -> "Stream":
        """Convert input audio volume to video output."""
        return self._apply_filter(
            filter_name="showvolume",
            inputs=[self],
            named_arguments={
                "rate": rate,
                "r": r,
                "b": b,
                "w": w,
                "h": h,
                "f": f,
                "c": c,
                "t": t,
                "v": v,
                "dm": dm,
                "dmc": dmc,
                "o": o,
                "s": s,
                "p": p,
                "m": m,
                "ds": ds,
            },
        )[0]

    def showwaves(
        self,
        size: str = None,
        s: str = None,
        mode: Literal["point", "line", "p2p", "cline"] | int = None,
        n: str = None,
        rate: str = None,
        r: str = None,
        split_channels: bool = None,
        colors: str = None,
        scale: Literal["lin", "log", "sqrt", "cbrt"] | int = None,
        draw: Literal["scale", "full"] | int = None,
    ) -> "Stream":
        """Convert input audio to a video output."""
        return self._apply_filter(
            filter_name="showwaves",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "mode": mode,
                "n": n,
                "rate": rate,
                "r": r,
                "split_channels": split_channels,
                "colors": colors,
                "scale": scale,
                "draw": draw,
            },
        )[0]

    def showwavespic(
        self,
        size: str = None,
        s: str = None,
        split_channels: bool = None,
        colors: str = None,
        scale: Literal["lin", "log", "sqrt", "cbrt"] | int = None,
        draw: Literal["scale", "full"] | int = None,
        filter: Literal["average", "peak"] | int = None,
    ) -> "Stream":
        """Convert input audio to a video output single picture."""
        return self._apply_filter(
            filter_name="showwavespic",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "split_channels": split_channels,
                "colors": colors,
                "scale": scale,
                "draw": draw,
                "filter": filter,
            },
        )[0]

    def shuffleframes(self, mapping: str = None) -> "Stream":
        """Shuffle video frames."""
        return self._apply_filter(
            filter_name="shuffleframes",
            inputs=[self],
            named_arguments={
                "mapping": mapping,
            },
        )[0]

    def shufflepixels(
        self,
        direction: Literal["forward", "inverse"] | int = None,
        d: Literal["forward", "inverse"] | int = None,
        mode: Literal["horizontal", "vertical", "block"] | int = None,
        m: Literal["horizontal", "vertical", "block"] | int = None,
        width: int = None,
        w: int = None,
        height: int = None,
        h: int = None,
        seed: str = None,
        s: str = None,
    ) -> "Stream":
        """Shuffle video pixels."""
        return self._apply_filter(
            filter_name="shufflepixels",
            inputs=[self],
            named_arguments={
                "direction": direction,
                "d": d,
                "mode": mode,
                "m": m,
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "seed": seed,
                "s": s,
            },
        )[0]

    def shuffleplanes(
        self, map0: int = None, map1: int = None, map2: int = None, map3: int = None
    ) -> "Stream":
        """Shuffle video planes."""
        return self._apply_filter(
            filter_name="shuffleplanes",
            inputs=[self],
            named_arguments={
                "map0": map0,
                "map1": map1,
                "map2": map2,
                "map3": map3,
            },
        )[0]

    def sidechaincompress(
        self,
        sidechain_stream: "Stream",
        level_in: float = None,
        mode: Literal["downward", "upward"] | int = None,
        threshold: float = None,
        ratio: float = None,
        attack: float = None,
        release: float = None,
        makeup: float = None,
        knee: float = None,
        link: Literal["average", "maximum"] | int = None,
        detection: Literal["peak", "rms"] | int = None,
        level_sc: float = None,
        mix: float = None,
    ) -> "Stream":
        """Sidechain compressor."""
        return self._apply_filter(
            filter_name="sidechaincompress",
            inputs=[self, sidechain_stream],
            named_arguments={
                "level_in": level_in,
                "mode": mode,
                "threshold": threshold,
                "ratio": ratio,
                "attack": attack,
                "release": release,
                "makeup": makeup,
                "knee": knee,
                "link": link,
                "detection": detection,
                "level_sc": level_sc,
                "mix": mix,
            },
        )[0]

    def sidechaingate(
        self,
        sidechain_stream: "Stream",
        level_in: float = None,
        mode: Literal["downward", "upward"] | int = None,
        range: float = None,
        threshold: float = None,
        ratio: float = None,
        attack: float = None,
        release: float = None,
        makeup: float = None,
        knee: float = None,
        detection: Literal["peak", "rms"] | int = None,
        link: Literal["average", "maximum"] | int = None,
        level_sc: float = None,
    ) -> "Stream":
        """Audio sidechain gate."""
        return self._apply_filter(
            filter_name="sidechaingate",
            inputs=[self, sidechain_stream],
            named_arguments={
                "level_in": level_in,
                "mode": mode,
                "range": range,
                "threshold": threshold,
                "ratio": ratio,
                "attack": attack,
                "release": release,
                "makeup": makeup,
                "knee": knee,
                "detection": detection,
                "link": link,
                "level_sc": level_sc,
            },
        )[0]

    def sidedata(
        self,
        mode: Literal["select", "delete"] | int = None,
        type: Literal[
            "PANSCAN",
            "A53_CC",
            "STEREO3D",
            "MATRIXENCODING",
            "DOWNMIX_INFO",
            "REPLAYGAIN",
            "DISPLAYMATRIX",
            "AFD",
            "MOTION_VECTORS",
            "SKIP_SAMPLES",
            "AUDIO_SERVICE_TYPE",
            "MASTERING_DISPLAY_METADATA",
            "GOP_TIMECODE",
            "SPHERICAL",
            "CONTENT_LIGHT_LEVEL",
            "ICC_PROFILE",
            "S12M_TIMECOD",
            "DYNAMIC_HDR_PLUS",
            "REGIONS_OF_INTEREST",
            "VIDEO_ENC_PARAMS",
            "SEI_UNREGISTERED",
            "FILM_GRAIN_PARAMS",
            "DETECTION_BOUNDING_BOXES",
            "DETECTION_BBOXES",
            "DOVI_RPU_BUFFER",
            "DOVI_METADATA",
            "DYNAMIC_HDR_VIVID",
            "AMBIENT_VIEWING_ENVIRONMENT",
            "VIDEO_HINT",
        ]
        | int = None,
    ) -> "Stream":
        """Manipulate video frame side data."""
        return self._apply_filter(
            filter_name="sidedata",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "type": type,
            },
        )[0]

    def signalstats(
        self,
        stat: Literal["tout", "vrep", "brng"] = None,
        out: Literal["tout", "vrep", "brng"] | int = None,
        c: str = None,
        color: str = None,
    ) -> "Stream":
        """Generate statistics from video analysis."""
        return self._apply_filter(
            filter_name="signalstats",
            inputs=[self],
            named_arguments={
                "stat": stat,
                "out": out,
                "c": c,
                "color": color,
            },
        )[0]

    def signature(
        self,
        *streams: "Stream",
        detectmode: Literal["off", "full", "fast"] | int = None,
        nb_inputs: int = None,
        filename: str = None,
        format: Literal["binary", "xml"] | int = None,
        th_d: int = None,
        th_dc: int = None,
        th_xh: int = None,
        th_di: int = None,
        th_it: float = None,
    ) -> "Stream":
        """Calculate the MPEG-7 video signature"""
        return self._apply_filter(
            filter_name="signature",
            inputs=[self, *streams],
            named_arguments={
                "detectmode": detectmode,
                "nb_inputs": nb_inputs,
                "filename": filename,
                "format": format,
                "th_d": th_d,
                "th_dc": th_dc,
                "th_xh": th_xh,
                "th_di": th_di,
                "th_it": th_it,
            },
        )[0]

    def silencedetect(
        self,
        n: float = None,
        noise: float = None,
        d: str = None,
        duration: str = None,
        mono: bool = None,
        m: bool = None,
    ) -> "Stream":
        """Detect silence."""
        return self._apply_filter(
            filter_name="silencedetect",
            inputs=[self],
            named_arguments={
                "n": n,
                "noise": noise,
                "d": d,
                "duration": duration,
                "mono": mono,
                "m": m,
            },
        )[0]

    def silenceremove(
        self,
        start_periods: int = None,
        start_duration: str = None,
        start_threshold: float = None,
        start_silence: str = None,
        start_mode: Literal["any", "all"] | int = None,
        stop_periods: int = None,
        stop_duration: str = None,
        stop_threshold: float = None,
        stop_silence: str = None,
        stop_mode: Literal["any", "all"] | int = None,
        detection: Literal["avg", "rms", "peak", "median", "ptp", "dev"] | int = None,
        window: str = None,
        timestamp: Literal["write", "copy"] | int = None,
    ) -> "Stream":
        """Remove silence."""
        return self._apply_filter(
            filter_name="silenceremove",
            inputs=[self],
            named_arguments={
                "start_periods": start_periods,
                "start_duration": start_duration,
                "start_threshold": start_threshold,
                "start_silence": start_silence,
                "start_mode": start_mode,
                "stop_periods": stop_periods,
                "stop_duration": stop_duration,
                "stop_threshold": stop_threshold,
                "stop_silence": stop_silence,
                "stop_mode": stop_mode,
                "detection": detection,
                "window": window,
                "timestamp": timestamp,
            },
        )[0]

    def siti(self, print_summary: bool = None) -> "Stream":
        """Calculate spatial information (SI) and temporal information (TI)."""
        return self._apply_filter(
            filter_name="siti",
            inputs=[self],
            named_arguments={
                "print_summary": print_summary,
            },
        )[0]

    def smartblur(
        self,
        luma_radius: float = None,
        lr: float = None,
        luma_strength: float = None,
        ls: float = None,
        luma_threshold: int = None,
        lt: int = None,
        chroma_radius: float = None,
        cr: float = None,
        chroma_strength: float = None,
        cs: float = None,
        chroma_threshold: int = None,
        ct: int = None,
        alpha_radius: float = None,
        ar: float = None,
        alpha_strength: float = None,
        as_: float = None,
        alpha_threshold: int = None,
        at: int = None,
    ) -> "Stream":
        """Blur the input video without impacting the outlines."""
        return self._apply_filter(
            filter_name="smartblur",
            inputs=[self],
            named_arguments={
                "luma_radius": luma_radius,
                "lr": lr,
                "luma_strength": luma_strength,
                "ls": ls,
                "luma_threshold": luma_threshold,
                "lt": lt,
                "chroma_radius": chroma_radius,
                "cr": cr,
                "chroma_strength": chroma_strength,
                "cs": cs,
                "chroma_threshold": chroma_threshold,
                "ct": ct,
                "alpha_radius": alpha_radius,
                "ar": ar,
                "alpha_strength": alpha_strength,
                "as": as_,
                "alpha_threshold": alpha_threshold,
                "at": at,
            },
        )[0]

    def sobel(
        self, planes: int = None, scale: float = None, delta: float = None
    ) -> "Stream":
        """Apply sobel operator."""
        return self._apply_filter(
            filter_name="sobel",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def spectrumsynth(
        self,
        phase_stream: "Stream",
        sample_rate: int = None,
        channels: int = None,
        scale: Literal["lin", "log"] | int = None,
        slide: Literal["replace", "scroll", "fullframe", "rscroll"] | int = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
        overlap: float = None,
        orientation: Literal["vertical", "horizontal"] | int = None,
    ) -> "Stream":
        """Convert input spectrum videos to audio output."""
        return self._apply_filter(
            filter_name="spectrumsynth",
            inputs=[self, phase_stream],
            named_arguments={
                "sample_rate": sample_rate,
                "channels": channels,
                "scale": scale,
                "slide": slide,
                "win_func": win_func,
                "overlap": overlap,
                "orientation": orientation,
            },
        )[0]

    def speechnorm(
        self,
        peak: float = None,
        p: float = None,
        expansion: float = None,
        e: float = None,
        compression: float = None,
        c: float = None,
        threshold: float = None,
        t: float = None,
        raise_: float = None,
        r: float = None,
        fall: float = None,
        f: float = None,
        channels: str = None,
        h: str = None,
        invert: bool = None,
        i: bool = None,
        link: bool = None,
        l: bool = None,
        rms: float = None,
        m: float = None,
    ) -> "Stream":
        """Speech Normalizer."""
        return self._apply_filter(
            filter_name="speechnorm",
            inputs=[self],
            named_arguments={
                "peak": peak,
                "p": p,
                "expansion": expansion,
                "e": e,
                "compression": compression,
                "c": c,
                "threshold": threshold,
                "t": t,
                "raise": raise_,
                "r": r,
                "fall": fall,
                "f": f,
                "channels": channels,
                "h": h,
                "invert": invert,
                "i": i,
                "link": link,
                "l": l,
                "rms": rms,
                "m": m,
            },
        )[0]

    def split(self, outputs: int = None) -> "FilterMultiOutput":
        """Pass on the input to N video outputs."""
        return self._apply_dynamic_outputs_filter(
            filter_name="split",
            inputs=[self],
            named_arguments={
                "outputs": outputs,
            },
        )

    def spp(
        self,
        quality: int = None,
        qp: int = None,
        mode: Literal["hard", "soft"] | int = None,
        use_bframe_qp: bool = None,
    ) -> "Stream":
        """Apply a simple post processing filter."""
        return self._apply_filter(
            filter_name="spp",
            inputs=[self],
            named_arguments={
                "quality": quality,
                "qp": qp,
                "mode": mode,
                "use_bframe_qp": use_bframe_qp,
            },
        )[0]

    def ssim(
        self, reference_stream: "Stream", stats_file: str = None, f: str = None
    ) -> "Stream":
        """Calculate the SSIM between two video streams."""
        return self._apply_filter(
            filter_name="ssim",
            inputs=[self, reference_stream],
            named_arguments={
                "stats_file": stats_file,
                "f": f,
            },
        )[0]

    def ssim360(
        self,
        reference_stream: "Stream",
        stats_file: str = None,
        f: str = None,
        compute_chroma: int = None,
        frame_skip_ratio: int = None,
        ref_projection: Literal[
            "e", "equirect", "c3x2", "c2x3", "barrel", "barrelsplit"
        ]
        | int = None,
        main_projection: Literal[
            "e", "equirect", "c3x2", "c2x3", "barrel", "barrelsplit"
        ]
        | int = None,
        ref_stereo: Literal["mono", "tb", "lr"] | int = None,
        main_stereo: Literal["mono", "tb", "lr"] | int = None,
        ref_pad: float = None,
        main_pad: float = None,
        use_tape: int = None,
        heatmap_str: str = None,
        default_heatmap_width: int = None,
        default_heatmap_height: int = None,
    ) -> "Stream":
        """Calculate the SSIM between two 360 video streams."""
        return self._apply_filter(
            filter_name="ssim360",
            inputs=[self, reference_stream],
            named_arguments={
                "stats_file": stats_file,
                "f": f,
                "compute_chroma": compute_chroma,
                "frame_skip_ratio": frame_skip_ratio,
                "ref_projection": ref_projection,
                "main_projection": main_projection,
                "ref_stereo": ref_stereo,
                "main_stereo": main_stereo,
                "ref_pad": ref_pad,
                "main_pad": main_pad,
                "use_tape": use_tape,
                "heatmap_str": heatmap_str,
                "default_heatmap_width": default_heatmap_width,
                "default_heatmap_height": default_heatmap_height,
            },
        )[0]

    def stereo3d(
        self,
        in_: Literal[
            "ab2l",
            "tb2l",
            "ab2r",
            "tb2r",
            "abl",
            "tbl",
            "abr",
            "tbr",
            "al",
            "ar",
            "sbs2l",
            "sbs2r",
            "sbsl",
            "sbsr",
            "irl",
            "irr",
            "icl",
            "icr",
        ]
        | int = None,
        out: Literal[
            "ab2l",
            "tb2l",
            "ab2r",
            "tb2r",
            "abl",
            "tbl",
            "abr",
            "tbr",
            "agmc",
            "agmd",
            "agmg",
            "agmh",
            "al",
            "ar",
            "arbg",
            "arcc",
            "arcd",
            "arcg",
            "arch",
            "argg",
            "aybc",
            "aybd",
            "aybg",
            "aybh",
            "irl",
            "irr",
            "ml",
            "mr",
            "sbs2l",
            "sbs2r",
            "sbsl",
            "sbsr",
            "chl",
            "chr",
            "icl",
            "icr",
            "hdmi",
        ]
        | int = None,
    ) -> "Stream":
        """Convert video stereoscopic 3D view."""
        return self._apply_filter(
            filter_name="stereo3d",
            inputs=[self],
            named_arguments={
                "in": in_,
                "out": out,
            },
        )[0]

    def stereotools(
        self,
        level_in: float = None,
        level_out: float = None,
        balance_in: float = None,
        balance_out: float = None,
        softclip: bool = None,
        mutel: bool = None,
        muter: bool = None,
        phasel: bool = None,
        phaser: bool = None,
        mode: Literal[
            "lr>lr",
            "lr>ms",
            "ms>lr",
            "lr>ll",
            "lr>rr",
            "lr>l+r",
            "lr>rl",
            "ms>ll",
            "ms>rr",
            "ms>rl",
            "lr>l-r",
        ]
        | int = None,
        slev: float = None,
        sbal: float = None,
        mlev: float = None,
        mpan: float = None,
        base: float = None,
        delay: float = None,
        sclevel: float = None,
        phase: float = None,
        bmode_in: Literal["balance", "amplitude", "power"] | int = None,
        bmode_out: Literal["balance", "amplitude", "power"] | int = None,
    ) -> "Stream":
        """Apply various stereo tools."""
        return self._apply_filter(
            filter_name="stereotools",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "balance_in": balance_in,
                "balance_out": balance_out,
                "softclip": softclip,
                "mutel": mutel,
                "muter": muter,
                "phasel": phasel,
                "phaser": phaser,
                "mode": mode,
                "slev": slev,
                "sbal": sbal,
                "mlev": mlev,
                "mpan": mpan,
                "base": base,
                "delay": delay,
                "sclevel": sclevel,
                "phase": phase,
                "bmode_in": bmode_in,
                "bmode_out": bmode_out,
            },
        )[0]

    def stereowiden(
        self,
        delay: float = None,
        feedback: float = None,
        crossfeed: float = None,
        drymix: float = None,
    ) -> "Stream":
        """Apply stereo widening effect."""
        return self._apply_filter(
            filter_name="stereowiden",
            inputs=[self],
            named_arguments={
                "delay": delay,
                "feedback": feedback,
                "crossfeed": crossfeed,
                "drymix": drymix,
            },
        )[0]

    def streamselect(
        self, *streams: "Stream", inputs: int = None, map: str = None
    ) -> "FilterMultiOutput":
        """Select video streams"""
        return self._apply_dynamic_outputs_filter(
            filter_name="streamselect",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "map": map,
            },
        )

    def subtitles(
        self,
        filename: str = None,
        f: str = None,
        original_size: str = None,
        fontsdir: str = None,
        alpha: bool = None,
        charenc: str = None,
        stream_index: int = None,
        si: int = None,
        force_style: str = None,
        wrap_unicode: bool = None,
    ) -> "Stream":
        """Render text subtitles onto input video using the libass library."""
        return self._apply_filter(
            filter_name="subtitles",
            inputs=[self],
            named_arguments={
                "filename": filename,
                "f": f,
                "original_size": original_size,
                "fontsdir": fontsdir,
                "alpha": alpha,
                "charenc": charenc,
                "stream_index": stream_index,
                "si": si,
                "force_style": force_style,
                "wrap_unicode": wrap_unicode,
            },
        )[0]

    def super2xsai(self) -> "Stream":
        """Scale the input by 2x using the Super2xSaI pixel art algorithm."""
        return self._apply_filter(
            filter_name="super2xsai", inputs=[self], named_arguments={}
        )[0]

    def superequalizer(
        self,
        _1b: float = None,
        _2b: float = None,
        _3b: float = None,
        _4b: float = None,
        _5b: float = None,
        _6b: float = None,
        _7b: float = None,
        _8b: float = None,
        _9b: float = None,
        _10b: float = None,
        _11b: float = None,
        _12b: float = None,
        _13b: float = None,
        _14b: float = None,
        _15b: float = None,
        _16b: float = None,
        _17b: float = None,
        _18b: float = None,
    ) -> "Stream":
        """Apply 18 band equalization filter."""
        return self._apply_filter(
            filter_name="superequalizer",
            inputs=[self],
            named_arguments={
                "1b": _1b,
                "2b": _2b,
                "3b": _3b,
                "4b": _4b,
                "5b": _5b,
                "6b": _6b,
                "7b": _7b,
                "8b": _8b,
                "9b": _9b,
                "10b": _10b,
                "11b": _11b,
                "12b": _12b,
                "13b": _13b,
                "14b": _14b,
                "15b": _15b,
                "16b": _16b,
                "17b": _17b,
                "18b": _18b,
            },
        )[0]

    def surround(
        self,
        chl_out: str = None,
        chl_in: str = None,
        level_in: float = None,
        level_out: float = None,
        lfe: bool = None,
        lfe_low: int = None,
        lfe_high: int = None,
        lfe_mode: Literal["add", "sub"] | int = None,
        smooth: float = None,
        angle: float = None,
        focus: float = None,
        fc_in: float = None,
        fc_out: float = None,
        fl_in: float = None,
        fl_out: float = None,
        fr_in: float = None,
        fr_out: float = None,
        sl_in: float = None,
        sl_out: float = None,
        sr_in: float = None,
        sr_out: float = None,
        bl_in: float = None,
        bl_out: float = None,
        br_in: float = None,
        br_out: float = None,
        bc_in: float = None,
        bc_out: float = None,
        lfe_in: float = None,
        lfe_out: float = None,
        allx: float = None,
        ally: float = None,
        fcx: float = None,
        flx: float = None,
        frx: float = None,
        blx: float = None,
        brx: float = None,
        slx: float = None,
        srx: float = None,
        bcx: float = None,
        fcy: float = None,
        fly: float = None,
        fry: float = None,
        bly: float = None,
        bry: float = None,
        sly: float = None,
        sry: float = None,
        bcy: float = None,
        win_size: int = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int = None,
        overlap: float = None,
    ) -> "Stream":
        """Apply audio surround upmix filter."""
        return self._apply_filter(
            filter_name="surround",
            inputs=[self],
            named_arguments={
                "chl_out": chl_out,
                "chl_in": chl_in,
                "level_in": level_in,
                "level_out": level_out,
                "lfe": lfe,
                "lfe_low": lfe_low,
                "lfe_high": lfe_high,
                "lfe_mode": lfe_mode,
                "smooth": smooth,
                "angle": angle,
                "focus": focus,
                "fc_in": fc_in,
                "fc_out": fc_out,
                "fl_in": fl_in,
                "fl_out": fl_out,
                "fr_in": fr_in,
                "fr_out": fr_out,
                "sl_in": sl_in,
                "sl_out": sl_out,
                "sr_in": sr_in,
                "sr_out": sr_out,
                "bl_in": bl_in,
                "bl_out": bl_out,
                "br_in": br_in,
                "br_out": br_out,
                "bc_in": bc_in,
                "bc_out": bc_out,
                "lfe_in": lfe_in,
                "lfe_out": lfe_out,
                "allx": allx,
                "ally": ally,
                "fcx": fcx,
                "flx": flx,
                "frx": frx,
                "blx": blx,
                "brx": brx,
                "slx": slx,
                "srx": srx,
                "bcx": bcx,
                "fcy": fcy,
                "fly": fly,
                "fry": fry,
                "bly": bly,
                "bry": bry,
                "sly": sly,
                "sry": sry,
                "bcy": bcy,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
            },
        )[0]

    def swaprect(
        self,
        w: str = None,
        h: str = None,
        x1: str = None,
        y1: str = None,
        x2: str = None,
        y2: str = None,
    ) -> "Stream":
        """Swap 2 rectangular objects in video."""
        return self._apply_filter(
            filter_name="swaprect",
            inputs=[self],
            named_arguments={
                "w": w,
                "h": h,
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
            },
        )[0]

    def swapuv(self) -> "Stream":
        """Swap U and V components."""
        return self._apply_filter(
            filter_name="swapuv", inputs=[self], named_arguments={}
        )[0]

    def tblend(
        self,
        c0_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        c1_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        c2_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        c3_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        all_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int = None,
        c0_expr: str = None,
        c1_expr: str = None,
        c2_expr: str = None,
        c3_expr: str = None,
        all_expr: str = None,
        c0_opacity: float = None,
        c1_opacity: float = None,
        c2_opacity: float = None,
        c3_opacity: float = None,
        all_opacity: float = None,
    ) -> "Stream":
        """Blend successive frames."""
        return self._apply_filter(
            filter_name="tblend",
            inputs=[self],
            named_arguments={
                "c0_mode": c0_mode,
                "c1_mode": c1_mode,
                "c2_mode": c2_mode,
                "c3_mode": c3_mode,
                "all_mode": all_mode,
                "c0_expr": c0_expr,
                "c1_expr": c1_expr,
                "c2_expr": c2_expr,
                "c3_expr": c3_expr,
                "all_expr": all_expr,
                "c0_opacity": c0_opacity,
                "c1_opacity": c1_opacity,
                "c2_opacity": c2_opacity,
                "c3_opacity": c3_opacity,
                "all_opacity": all_opacity,
            },
        )[0]

    def telecine(
        self,
        first_field: Literal["top", "t", "bottom", "b"] | int = None,
        pattern: str = None,
    ) -> "Stream":
        """Apply a telecine pattern."""
        return self._apply_filter(
            filter_name="telecine",
            inputs=[self],
            named_arguments={
                "first_field": first_field,
                "pattern": pattern,
            },
        )[0]

    def thistogram(
        self,
        width: int = None,
        w: int = None,
        display_mode: Literal["overlay", "parade", "stack"] | int = None,
        d: Literal["overlay", "parade", "stack"] | int = None,
        levels_mode: Literal["linear", "logarithmic"] | int = None,
        m: Literal["linear", "logarithmic"] | int = None,
        components: int = None,
        c: int = None,
        bgopacity: float = None,
        b: float = None,
        envelope: bool = None,
        e: bool = None,
        ecolor: str = None,
        ec: str = None,
        slide: Literal["frame", "replace", "scroll", "rscroll", "picture"] | int = None,
    ) -> "Stream":
        """Compute and draw a temporal histogram."""
        return self._apply_filter(
            filter_name="thistogram",
            inputs=[self],
            named_arguments={
                "width": width,
                "w": w,
                "display_mode": display_mode,
                "d": d,
                "levels_mode": levels_mode,
                "m": m,
                "components": components,
                "c": c,
                "bgopacity": bgopacity,
                "b": b,
                "envelope": envelope,
                "e": e,
                "ecolor": ecolor,
                "ec": ec,
                "slide": slide,
            },
        )[0]

    def threshold(
        self,
        threshold_stream: "Stream",
        min_stream: "Stream",
        max_stream: "Stream",
        planes: int = None,
    ) -> "Stream":
        """Threshold first video stream using other video streams."""
        return self._apply_filter(
            filter_name="threshold",
            inputs=[self, threshold_stream, min_stream, max_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def thumbnail(
        self, n: int = None, log: Literal["quiet", "info", "verbose"] | int = None
    ) -> "Stream":
        """Select the most representative frame in a given sequence of consecutive frames."""
        return self._apply_filter(
            filter_name="thumbnail",
            inputs=[self],
            named_arguments={
                "n": n,
                "log": log,
            },
        )[0]

    def tile(
        self,
        layout: str = None,
        nb_frames: int = None,
        margin: int = None,
        padding: int = None,
        color: str = None,
        overlap: int = None,
        init_padding: int = None,
    ) -> "Stream":
        """Tile several successive frames together."""
        return self._apply_filter(
            filter_name="tile",
            inputs=[self],
            named_arguments={
                "layout": layout,
                "nb_frames": nb_frames,
                "margin": margin,
                "padding": padding,
                "color": color,
                "overlap": overlap,
                "init_padding": init_padding,
            },
        )[0]

    def tiltandshift(
        self,
        _tilt: int = None,
        _start: Literal["none", "frame", "black"] | int = None,
        _end: Literal["none", "frame", "black"] | int = None,
        _hold: int = None,
        _pad: int = None,
    ) -> "Stream":
        """Generate a tilt-and-shift'd video."""
        return self._apply_filter(
            filter_name="tiltandshift",
            inputs=[self],
            named_arguments={
                "-tilt": _tilt,
                "-start": _start,
                "-end": _end,
                "-hold": _hold,
                "-pad": _pad,
            },
        )[0]

    def tiltshelf(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        gain: float = None,
        g: float = None,
        poles: int = None,
        p: int = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Apply a tilt shelf filter."""
        return self._apply_filter(
            filter_name="tiltshelf",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def tinterlace(
        self,
        mode: Literal[
            "merge",
            "drop_even",
            "drop_odd",
            "pad",
            "interleave_top",
            "interleave_bottom",
            "interlacex2",
            "mergex2",
        ]
        | int = None,
    ) -> "Stream":
        """Perform temporal field interlacing."""
        return self._apply_filter(
            filter_name="tinterlace",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def tlut2(
        self, c0: str = None, c1: str = None, c2: str = None, c3: str = None
    ) -> "Stream":
        """Compute and apply a lookup table from two successive frames."""
        return self._apply_filter(
            filter_name="tlut2",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
            },
        )[0]

    def tmedian(
        self, radius: int = None, planes: int = None, percentile: float = None
    ) -> "Stream":
        """Pick median pixels from successive frames."""
        return self._apply_filter(
            filter_name="tmedian",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "planes": planes,
                "percentile": percentile,
            },
        )[0]

    def tmidequalizer(
        self, radius: int = None, sigma: float = None, planes: int = None
    ) -> "Stream":
        """Apply Temporal Midway Equalization."""
        return self._apply_filter(
            filter_name="tmidequalizer",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "sigma": sigma,
                "planes": planes,
            },
        )[0]

    def tmix(
        self,
        frames: int = None,
        weights: str = None,
        scale: float = None,
        planes: str = None,
    ) -> "Stream":
        """Mix successive video frames."""
        return self._apply_filter(
            filter_name="tmix",
            inputs=[self],
            named_arguments={
                "frames": frames,
                "weights": weights,
                "scale": scale,
                "planes": planes,
            },
        )[0]

    def tonemap(
        self,
        tonemap: Literal[
            "none", "linear", "gamma", "clip", "reinhard", "hable", "mobius"
        ]
        | int = None,
        param: float = None,
        desat: float = None,
        peak: float = None,
    ) -> "Stream":
        """Conversion to/from different dynamic ranges."""
        return self._apply_filter(
            filter_name="tonemap",
            inputs=[self],
            named_arguments={
                "tonemap": tonemap,
                "param": param,
                "desat": desat,
                "peak": peak,
            },
        )[0]

    def tpad(
        self,
        start: int = None,
        stop: int = None,
        start_mode: Literal["add", "clone"] | int = None,
        stop_mode: Literal["add", "clone"] | int = None,
        start_duration: str = None,
        stop_duration: str = None,
        color: str = None,
    ) -> "Stream":
        """Temporarily pad video frames."""
        return self._apply_filter(
            filter_name="tpad",
            inputs=[self],
            named_arguments={
                "start": start,
                "stop": stop,
                "start_mode": start_mode,
                "stop_mode": stop_mode,
                "start_duration": start_duration,
                "stop_duration": stop_duration,
                "color": color,
            },
        )[0]

    def transpose(
        self,
        dir: Literal["cclock_flip", "clock", "cclock", "clock_flip"] | int = None,
        passthrough: Literal["none", "portrait", "landscape"] | int = None,
    ) -> "Stream":
        """Transpose input video."""
        return self._apply_filter(
            filter_name="transpose",
            inputs=[self],
            named_arguments={
                "dir": dir,
                "passthrough": passthrough,
            },
        )[0]

    def transpose_vt(
        self,
        dir: Literal[
            "cclock_flip", "clock", "cclock", "clock_flip", "reversal", "hflip", "vflip"
        ]
        | int = None,
        passthrough: Literal["none", "portrait", "landscape"] | int = None,
    ) -> "Stream":
        """Transpose Videotoolbox frames"""
        return self._apply_filter(
            filter_name="transpose_vt",
            inputs=[self],
            named_arguments={
                "dir": dir,
                "passthrough": passthrough,
            },
        )[0]

    def treble(
        self,
        frequency: float = None,
        f: float = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int = None,
        t: Literal["h", "q", "o", "s", "k"] | int = None,
        width: float = None,
        w: float = None,
        gain: float = None,
        g: float = None,
        poles: int = None,
        p: int = None,
        mix: float = None,
        m: float = None,
        channels: str = None,
        c: str = None,
        normalize: bool = None,
        n: bool = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"] | int = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int = None,
        blocksize: int = None,
        b: int = None,
    ) -> "Stream":
        """Boost or cut upper frequencies."""
        return self._apply_filter(
            filter_name="treble",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def tremolo(self, f: float = None, d: float = None) -> "Stream":
        """Apply tremolo effect."""
        return self._apply_filter(
            filter_name="tremolo",
            inputs=[self],
            named_arguments={
                "f": f,
                "d": d,
            },
        )[0]

    def trim(
        self,
        start: str = None,
        starti: str = None,
        end: str = None,
        endi: str = None,
        start_pts: str = None,
        end_pts: str = None,
        duration: str = None,
        durationi: str = None,
        start_frame: str = None,
        end_frame: str = None,
    ) -> "Stream":
        """Pick one continuous section from the input, drop the rest."""
        return self._apply_filter(
            filter_name="trim",
            inputs=[self],
            named_arguments={
                "start": start,
                "starti": starti,
                "end": end,
                "endi": endi,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "durationi": durationi,
                "start_frame": start_frame,
                "end_frame": end_frame,
            },
        )[0]

    def unpremultiply(
        self, *streams: "Stream", planes: int = None, inplace: bool = None
    ) -> "Stream":
        """UnPreMultiply first stream with first plane of second stream."""
        return self._apply_filter(
            filter_name="unpremultiply",
            inputs=[self, *streams],
            named_arguments={
                "planes": planes,
                "inplace": inplace,
            },
        )[0]

    def unsharp(
        self,
        luma_msize_x: int = None,
        lx: int = None,
        luma_msize_y: int = None,
        ly: int = None,
        luma_amount: float = None,
        la: float = None,
        chroma_msize_x: int = None,
        cx: int = None,
        chroma_msize_y: int = None,
        cy: int = None,
        chroma_amount: float = None,
        ca: float = None,
        alpha_msize_x: int = None,
        ax: int = None,
        alpha_msize_y: int = None,
        ay: int = None,
        alpha_amount: float = None,
        aa: float = None,
    ) -> "Stream":
        """Sharpen or blur the input video."""
        return self._apply_filter(
            filter_name="unsharp",
            inputs=[self],
            named_arguments={
                "luma_msize_x": luma_msize_x,
                "lx": lx,
                "luma_msize_y": luma_msize_y,
                "ly": ly,
                "luma_amount": luma_amount,
                "la": la,
                "chroma_msize_x": chroma_msize_x,
                "cx": cx,
                "chroma_msize_y": chroma_msize_y,
                "cy": cy,
                "chroma_amount": chroma_amount,
                "ca": ca,
                "alpha_msize_x": alpha_msize_x,
                "ax": ax,
                "alpha_msize_y": alpha_msize_y,
                "ay": ay,
                "alpha_amount": alpha_amount,
                "aa": aa,
            },
        )[0]

    def untile(self, layout: str = None) -> "Stream":
        """Untile a frame into a sequence of frames."""
        return self._apply_filter(
            filter_name="untile",
            inputs=[self],
            named_arguments={
                "layout": layout,
            },
        )[0]

    def uspp(
        self,
        quality: int = None,
        qp: int = None,
        use_bframe_qp: bool = None,
        codec: str = None,
    ) -> "Stream":
        """Apply Ultra Simple / Slow Post-processing filter."""
        return self._apply_filter(
            filter_name="uspp",
            inputs=[self],
            named_arguments={
                "quality": quality,
                "qp": qp,
                "use_bframe_qp": use_bframe_qp,
                "codec": codec,
            },
        )[0]

    def v360(
        self,
        input: Literal[
            "e",
            "equirect",
            "c3x2",
            "c6x1",
            "eac",
            "dfisheye",
            "flat",
            "rectilinear",
            "gnomonic",
            "barrel",
            "fb",
            "c1x6",
            "sg",
            "mercator",
            "ball",
            "hammer",
            "sinusoidal",
            "fisheye",
            "pannini",
            "cylindrical",
            "tetrahedron",
            "barrelsplit",
            "tsp",
            "hequirect",
            "he",
            "equisolid",
            "og",
            "octahedron",
            "cylindricalea",
        ]
        | int = None,
        output: Literal[
            "e",
            "equirect",
            "c3x2",
            "c6x1",
            "eac",
            "dfisheye",
            "flat",
            "rectilinear",
            "gnomonic",
            "barrel",
            "fb",
            "c1x6",
            "sg",
            "mercator",
            "ball",
            "hammer",
            "sinusoidal",
            "fisheye",
            "pannini",
            "cylindrical",
            "perspective",
            "tetrahedron",
            "barrelsplit",
            "tsp",
            "hequirect",
            "he",
            "equisolid",
            "og",
            "octahedron",
            "cylindricalea",
        ]
        | int = None,
        interp: Literal[
            "near",
            "nearest",
            "line",
            "linear",
            "lagrange9",
            "cube",
            "cubic",
            "lanc",
            "lanczos",
            "sp16",
            "spline16",
            "gauss",
            "gaussian",
            "mitchell",
        ]
        | int = None,
        w: int = None,
        h: int = None,
        in_stereo: Literal["2d", "sbs", "tb"] | int = None,
        out_stereo: Literal["2d", "sbs", "tb"] | int = None,
        in_forder: str = None,
        out_forder: str = None,
        in_frot: str = None,
        out_frot: str = None,
        in_pad: float = None,
        out_pad: float = None,
        fin_pad: int = None,
        fout_pad: int = None,
        yaw: float = None,
        pitch: float = None,
        roll: float = None,
        rorder: str = None,
        h_fov: float = None,
        v_fov: float = None,
        d_fov: float = None,
        h_flip: bool = None,
        v_flip: bool = None,
        d_flip: bool = None,
        ih_flip: bool = None,
        iv_flip: bool = None,
        in_trans: bool = None,
        out_trans: bool = None,
        ih_fov: float = None,
        iv_fov: float = None,
        id_fov: float = None,
        h_offset: float = None,
        v_offset: float = None,
        alpha_mask: bool = None,
        reset_rot: bool = None,
    ) -> "Stream":
        """Convert 360 projection of video."""
        return self._apply_filter(
            filter_name="v360",
            inputs=[self],
            named_arguments={
                "input": input,
                "output": output,
                "interp": interp,
                "w": w,
                "h": h,
                "in_stereo": in_stereo,
                "out_stereo": out_stereo,
                "in_forder": in_forder,
                "out_forder": out_forder,
                "in_frot": in_frot,
                "out_frot": out_frot,
                "in_pad": in_pad,
                "out_pad": out_pad,
                "fin_pad": fin_pad,
                "fout_pad": fout_pad,
                "yaw": yaw,
                "pitch": pitch,
                "roll": roll,
                "rorder": rorder,
                "h_fov": h_fov,
                "v_fov": v_fov,
                "d_fov": d_fov,
                "h_flip": h_flip,
                "v_flip": v_flip,
                "d_flip": d_flip,
                "ih_flip": ih_flip,
                "iv_flip": iv_flip,
                "in_trans": in_trans,
                "out_trans": out_trans,
                "ih_fov": ih_fov,
                "iv_fov": iv_fov,
                "id_fov": id_fov,
                "h_offset": h_offset,
                "v_offset": v_offset,
                "alpha_mask": alpha_mask,
                "reset_rot": reset_rot,
            },
        )[0]

    def vaguedenoiser(
        self,
        threshold: float = None,
        method: Literal["hard", "soft", "garrote"] | int = None,
        nsteps: int = None,
        percent: float = None,
        planes: int = None,
        type: Literal["universal", "bayes"] | int = None,
    ) -> "Stream":
        """Apply a Wavelet based Denoiser."""
        return self._apply_filter(
            filter_name="vaguedenoiser",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "method": method,
                "nsteps": nsteps,
                "percent": percent,
                "planes": planes,
                "type": type,
            },
        )[0]

    def varblur(
        self,
        radius_stream: "Stream",
        min_r: int = None,
        max_r: int = None,
        planes: int = None,
    ) -> "Stream":
        """Apply Variable Blur filter."""
        return self._apply_filter(
            filter_name="varblur",
            inputs=[self, radius_stream],
            named_arguments={
                "min_r": min_r,
                "max_r": max_r,
                "planes": planes,
            },
        )[0]

    def vectorscope(
        self,
        mode: Literal["gray", "tint", "color", "color2", "color3", "color4", "color5"]
        | int = None,
        m: Literal["gray", "tint", "color", "color2", "color3", "color4", "color5"]
        | int = None,
        x: int = None,
        y: int = None,
        intensity: float = None,
        i: float = None,
        envelope: Literal["none", "instant", "peak", "peak+instant"] | int = None,
        e: Literal["none", "instant", "peak", "peak+instant"] | int = None,
        graticule: Literal["none", "green", "color", "invert"] | int = None,
        g: Literal["none", "green", "color", "invert"] | int = None,
        opacity: float = None,
        o: float = None,
        flags: Literal["white", "black", "name"] = None,
        f: Literal["white", "black", "name"] = None,
        bgopacity: float = None,
        b: float = None,
        lthreshold: float = None,
        l: float = None,
        hthreshold: float = None,
        h: float = None,
        colorspace: Literal["auto", "601", "709"] | int = None,
        c: Literal["auto", "601", "709"] | int = None,
        tint0: float = None,
        t0: float = None,
        tint1: float = None,
        t1: float = None,
    ) -> "Stream":
        """Video vectorscope."""
        return self._apply_filter(
            filter_name="vectorscope",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "m": m,
                "x": x,
                "y": y,
                "intensity": intensity,
                "i": i,
                "envelope": envelope,
                "e": e,
                "graticule": graticule,
                "g": g,
                "opacity": opacity,
                "o": o,
                "flags": flags,
                "f": f,
                "bgopacity": bgopacity,
                "b": b,
                "lthreshold": lthreshold,
                "l": l,
                "hthreshold": hthreshold,
                "h": h,
                "colorspace": colorspace,
                "c": c,
                "tint0": tint0,
                "t0": t0,
                "tint1": tint1,
                "t1": t1,
            },
        )[0]

    def vflip(self) -> "Stream":
        """Flip the input video vertically."""
        return self._apply_filter(
            filter_name="vflip", inputs=[self], named_arguments={}
        )[0]

    def vfrdet(self) -> "Stream":
        """Variable frame rate detect filter."""
        return self._apply_filter(
            filter_name="vfrdet", inputs=[self], named_arguments={}
        )[0]

    def vibrance(
        self,
        intensity: float = None,
        rbal: float = None,
        gbal: float = None,
        bbal: float = None,
        rlum: float = None,
        glum: float = None,
        blum: float = None,
        alternate: bool = None,
    ) -> "Stream":
        """Boost or alter saturation."""
        return self._apply_filter(
            filter_name="vibrance",
            inputs=[self],
            named_arguments={
                "intensity": intensity,
                "rbal": rbal,
                "gbal": gbal,
                "bbal": bbal,
                "rlum": rlum,
                "glum": glum,
                "blum": blum,
                "alternate": alternate,
            },
        )[0]

    def vibrato(self, f: float = None, d: float = None) -> "Stream":
        """Apply vibrato effect."""
        return self._apply_filter(
            filter_name="vibrato",
            inputs=[self],
            named_arguments={
                "f": f,
                "d": d,
            },
        )[0]

    def vidstabdetect(
        self,
        result: str = None,
        shakiness: int = None,
        accuracy: int = None,
        stepsize: int = None,
        mincontrast: float = None,
        show: int = None,
        tripod: int = None,
        fileformat: Literal["ascii", "binary"] | int = None,
    ) -> "Stream":
        """Extract relative transformations, pass 1 of 2 for stabilization (see vidstabtransform for pass 2)."""
        return self._apply_filter(
            filter_name="vidstabdetect",
            inputs=[self],
            named_arguments={
                "result": result,
                "shakiness": shakiness,
                "accuracy": accuracy,
                "stepsize": stepsize,
                "mincontrast": mincontrast,
                "show": show,
                "tripod": tripod,
                "fileformat": fileformat,
            },
        )[0]

    def vidstabtransform(
        self,
        input: str = None,
        smoothing: int = None,
        optalgo: Literal["opt", "gauss", "avg"] | int = None,
        maxshift: int = None,
        maxangle: float = None,
        crop: Literal["keep", "black"] | int = None,
        invert: int = None,
        relative: int = None,
        zoom: float = None,
        optzoom: int = None,
        zoomspeed: float = None,
        interpol: Literal["no", "linear", "bilinear", "bicubic"] | int = None,
        tripod: bool = None,
        debug: bool = None,
    ) -> "Stream":
        """Transform the frames, pass 2 of 2 for stabilization (see vidstabdetect for pass 1)."""
        return self._apply_filter(
            filter_name="vidstabtransform",
            inputs=[self],
            named_arguments={
                "input": input,
                "smoothing": smoothing,
                "optalgo": optalgo,
                "maxshift": maxshift,
                "maxangle": maxangle,
                "crop": crop,
                "invert": invert,
                "relative": relative,
                "zoom": zoom,
                "optzoom": optzoom,
                "zoomspeed": zoomspeed,
                "interpol": interpol,
                "tripod": tripod,
                "debug": debug,
            },
        )[0]

    def vif(self, reference_stream: "Stream") -> "Stream":
        """Calculate the VIF between two video streams."""
        return self._apply_filter(
            filter_name="vif", inputs=[self, reference_stream], named_arguments={}
        )[0]

    def vignette(
        self,
        angle: str = None,
        a: str = None,
        x0: str = None,
        y0: str = None,
        mode: Literal["forward", "backward"] | int = None,
        eval: Literal["init", "frame"] | int = None,
        dither: bool = None,
        aspect: str = None,
    ) -> "Stream":
        """Make or reverse a vignette effect."""
        return self._apply_filter(
            filter_name="vignette",
            inputs=[self],
            named_arguments={
                "angle": angle,
                "a": a,
                "x0": x0,
                "y0": y0,
                "mode": mode,
                "eval": eval,
                "dither": dither,
                "aspect": aspect,
            },
        )[0]

    def virtualbass(self, cutoff: float = None, strength: float = None) -> "Stream":
        """Audio Virtual Bass."""
        return self._apply_filter(
            filter_name="virtualbass",
            inputs=[self],
            named_arguments={
                "cutoff": cutoff,
                "strength": strength,
            },
        )[0]

    def vmafmotion(self, stats_file: str = None) -> "Stream":
        """Calculate the VMAF Motion score."""
        return self._apply_filter(
            filter_name="vmafmotion",
            inputs=[self],
            named_arguments={
                "stats_file": stats_file,
            },
        )[0]

    def volume(
        self,
        volume: str = None,
        precision: Literal["fixed", "float", "double"] | int = None,
        eval: Literal["once", "frame"] | int = None,
        replaygain: Literal["drop", "ignore", "track", "album"] | int = None,
        replaygain_preamp: float = None,
        replaygain_noclip: bool = None,
    ) -> "Stream":
        """Change input volume."""
        return self._apply_filter(
            filter_name="volume",
            inputs=[self],
            named_arguments={
                "volume": volume,
                "precision": precision,
                "eval": eval,
                "replaygain": replaygain,
                "replaygain_preamp": replaygain_preamp,
                "replaygain_noclip": replaygain_noclip,
            },
        )[0]

    def volumedetect(self) -> "Stream":
        """Detect audio volume."""
        return self._apply_filter(
            filter_name="volumedetect", inputs=[self], named_arguments={}
        )[0]

    def vstack(
        self, *streams: "Stream", inputs: int = None, shortest: bool = None
    ) -> "Stream":
        """Stack video inputs vertically."""
        return self._apply_filter(
            filter_name="vstack",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "shortest": shortest,
            },
        )[0]

    def w3fdif(
        self,
        filter: Literal["simple", "complex"] | int = None,
        mode: Literal["frame", "field"] | int = None,
        parity: Literal["tff", "bff", "auto"] | int = None,
        deint: Literal["all", "interlaced"] | int = None,
    ) -> "Stream":
        """Apply Martin Weston three field deinterlace."""
        return self._apply_filter(
            filter_name="w3fdif",
            inputs=[self],
            named_arguments={
                "filter": filter,
                "mode": mode,
                "parity": parity,
                "deint": deint,
            },
        )[0]

    def waveform(
        self,
        mode: Literal["row", "column"] | int = None,
        m: Literal["row", "column"] | int = None,
        intensity: float = None,
        i: float = None,
        mirror: bool = None,
        r: bool = None,
        display: Literal["overlay", "stack", "parade"] | int = None,
        d: Literal["overlay", "stack", "parade"] | int = None,
        components: int = None,
        c: int = None,
        envelope: Literal["none", "instant", "peak", "peak+instant"] | int = None,
        e: Literal["none", "instant", "peak", "peak+instant"] | int = None,
        filter: Literal[
            "lowpass", "flat", "aflat", "chroma", "color", "acolor", "xflat", "yflat"
        ]
        | int = None,
        f: Literal[
            "lowpass", "flat", "aflat", "chroma", "color", "acolor", "xflat", "yflat"
        ]
        | int = None,
        graticule: Literal["none", "green", "orange", "invert"] | int = None,
        g: Literal["none", "green", "orange", "invert"] | int = None,
        opacity: float = None,
        o: float = None,
        flags: Literal["numbers", "dots"] = None,
        fl: Literal["numbers", "dots"] = None,
        scale: Literal["digital", "millivolts", "ire"] | int = None,
        s: Literal["digital", "millivolts", "ire"] | int = None,
        bgopacity: float = None,
        b: float = None,
        tint0: float = None,
        t0: float = None,
        tint1: float = None,
        t1: float = None,
        fitmode: Literal["none", "size"] | int = None,
        fm: Literal["none", "size"] | int = None,
        input: Literal["all", "first"] | int = None,
    ) -> "Stream":
        """Video waveform monitor."""
        return self._apply_filter(
            filter_name="waveform",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "m": m,
                "intensity": intensity,
                "i": i,
                "mirror": mirror,
                "r": r,
                "display": display,
                "d": d,
                "components": components,
                "c": c,
                "envelope": envelope,
                "e": e,
                "filter": filter,
                "f": f,
                "graticule": graticule,
                "g": g,
                "opacity": opacity,
                "o": o,
                "flags": flags,
                "fl": fl,
                "scale": scale,
                "s": s,
                "bgopacity": bgopacity,
                "b": b,
                "tint0": tint0,
                "t0": t0,
                "tint1": tint1,
                "t1": t1,
                "fitmode": fitmode,
                "fm": fm,
                "input": input,
            },
        )[0]

    def weave(
        self, first_field: Literal["top", "t", "bottom", "b"] | int = None
    ) -> "Stream":
        """Weave input video fields into frames."""
        return self._apply_filter(
            filter_name="weave",
            inputs=[self],
            named_arguments={
                "first_field": first_field,
            },
        )[0]

    def xbr(self, n: int = None) -> "Stream":
        """Scale the input using xBR algorithm."""
        return self._apply_filter(
            filter_name="xbr",
            inputs=[self],
            named_arguments={
                "n": n,
            },
        )[0]

    def xcorrelate(
        self,
        secondary_stream: "Stream",
        planes: int = None,
        secondary: Literal["first", "all"] | int = None,
    ) -> "Stream":
        """Cross-correlate first video stream with second video stream."""
        return self._apply_filter(
            filter_name="xcorrelate",
            inputs=[self, secondary_stream],
            named_arguments={
                "planes": planes,
                "secondary": secondary,
            },
        )[0]

    def xfade(
        self,
        xfade_stream: "Stream",
        transition: Literal[
            "custom",
            "fade",
            "wipeleft",
            "wiperight",
            "wipeup",
            "wipedown",
            "slideleft",
            "slideright",
            "slideup",
            "slidedown",
            "circlecrop",
            "rectcrop",
            "distance",
            "fadeblack",
            "fadewhite",
            "radial",
            "smoothleft",
            "smoothright",
            "smoothup",
            "smoothdown",
            "circleopen",
            "circleclose",
            "vertopen",
            "vertclose",
            "horzopen",
            "horzclose",
            "dissolve",
            "pixelize",
            "diagtl",
            "diagtr",
            "diagbl",
            "diagbr",
            "hlslice",
            "hrslice",
            "vuslice",
            "vdslice",
            "hblur",
            "fadegrays",
            "wipetl",
            "wipetr",
            "wipebl",
            "wipebr",
            "squeezeh",
            "squeezev",
            "zoomin",
            "fadefast",
            "fadeslow",
            "hlwind",
            "hrwind",
            "vuwind",
            "vdwind",
            "coverleft",
            "coverright",
            "coverup",
            "coverdown",
            "revealleft",
            "revealright",
            "revealup",
            "revealdown",
        ]
        | int = None,
        duration: str = None,
        offset: str = None,
        expr: str = None,
    ) -> "Stream":
        """Cross fade one video with another video."""
        return self._apply_filter(
            filter_name="xfade",
            inputs=[self, xfade_stream],
            named_arguments={
                "transition": transition,
                "duration": duration,
                "offset": offset,
                "expr": expr,
            },
        )[0]

    def xmedian(
        self,
        *streams: "Stream",
        inputs: int = None,
        planes: int = None,
        percentile: float = None,
    ) -> "Stream":
        """Pick median pixels from several video inputs."""
        return self._apply_filter(
            filter_name="xmedian",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "planes": planes,
                "percentile": percentile,
            },
        )[0]

    def xpsnr(
        self, reference_stream: "Stream", stats_file: str = None, f: str = None
    ) -> "Stream":
        """Calculate the extended perceptually weighted peak signal-to-noise ratio (XPSNR) between two video streams."""
        return self._apply_filter(
            filter_name="xpsnr",
            inputs=[self, reference_stream],
            named_arguments={
                "stats_file": stats_file,
                "f": f,
            },
        )[0]

    def xstack(
        self,
        *streams: "Stream",
        inputs: int = None,
        layout: str = None,
        grid: str = None,
        shortest: bool = None,
        fill: str = None,
    ) -> "Stream":
        """Stack video inputs into custom layout."""
        return self._apply_filter(
            filter_name="xstack",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "layout": layout,
                "grid": grid,
                "shortest": shortest,
                "fill": fill,
            },
        )[0]

    def yadif(
        self,
        mode: Literal[
            "send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"
        ]
        | int = None,
        parity: Literal["tff", "bff", "auto"] | int = None,
        deint: Literal["all", "interlaced"] | int = None,
    ) -> "Stream":
        """Deinterlace the input image."""
        return self._apply_filter(
            filter_name="yadif",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "parity": parity,
                "deint": deint,
            },
        )[0]

    def yaepblur(
        self,
        radius: int = None,
        r: int = None,
        planes: int = None,
        p: int = None,
        sigma: int = None,
        s: int = None,
    ) -> "Stream":
        """Yet another edge preserving blur filter."""
        return self._apply_filter(
            filter_name="yaepblur",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "r": r,
                "planes": planes,
                "p": p,
                "sigma": sigma,
                "s": s,
            },
        )[0]

    def zmq(self, bind_address: str = None, b: str = None) -> "Stream":
        """Receive commands through ZMQ and broker them to filters."""
        return self._apply_filter(
            filter_name="zmq",
            inputs=[self],
            named_arguments={
                "bind_address": bind_address,
                "b": b,
            },
        )[0]

    def zoompan(
        self,
        zoom: str = None,
        z: str = None,
        x: str = None,
        y: str = None,
        d: str = None,
        s: str = None,
        fps: str = None,
    ) -> "Stream":
        """Apply Zoom & Pan effect."""
        return self._apply_filter(
            filter_name="zoompan",
            inputs=[self],
            named_arguments={
                "zoom": zoom,
                "z": z,
                "x": x,
                "y": y,
                "d": d,
                "s": s,
                "fps": fps,
            },
        )[0]

    def zscale(
        self,
        w: str = None,
        width: str = None,
        h: str = None,
        height: str = None,
        size: str = None,
        s: str = None,
        dither: Literal["none", "ordered", "random", "error_diffusion"] | int = None,
        d: Literal["none", "ordered", "random", "error_diffusion"] | int = None,
        filter: Literal[
            "point", "bilinear", "bicubic", "spline16", "spline36", "lanczos"
        ]
        | int = None,
        f: Literal["point", "bilinear", "bicubic", "spline16", "spline36", "lanczos"]
        | int = None,
        out_range: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int = None,
        range: Literal["input", "limited", "full", "unknown", "tv", "pc"] | int = None,
        r: Literal["input", "limited", "full", "unknown", "tv", "pc"] | int = None,
        primaries: Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        p: Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        transfer: Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | int = None,
        t: Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | int = None,
        matrix: Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | int = None,
        m: Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | int = None,
        in_range: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int = None,
        rangein: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int = None,
        rin: Literal["input", "limited", "full", "unknown", "tv", "pc"] | int = None,
        primariesin: Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        pin: Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int = None,
        transferin: Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | int = None,
        tin: Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | int = None,
        matrixin: Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | int = None,
        min: Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | int = None,
        chromal: Literal[
            "input", "left", "center", "topleft", "top", "bottomleft", "bottom"
        ]
        | int = None,
        c: Literal["input", "left", "center", "topleft", "top", "bottomleft", "bottom"]
        | int = None,
        chromalin: Literal[
            "input", "left", "center", "topleft", "top", "bottomleft", "bottom"
        ]
        | int = None,
        cin: Literal[
            "input", "left", "center", "topleft", "top", "bottomleft", "bottom"
        ]
        | int = None,
        npl: float = None,
        agamma: bool = None,
        param_a: float = None,
        param_b: float = None,
    ) -> "Stream":
        """Apply resizing, colorspace and bit depth conversion."""
        return self._apply_filter(
            filter_name="zscale",
            inputs=[self],
            named_arguments={
                "w": w,
                "width": width,
                "h": h,
                "height": height,
                "size": size,
                "s": s,
                "dither": dither,
                "d": d,
                "filter": filter,
                "f": f,
                "out_range": out_range,
                "range": range,
                "r": r,
                "primaries": primaries,
                "p": p,
                "transfer": transfer,
                "t": t,
                "matrix": matrix,
                "m": m,
                "in_range": in_range,
                "rangein": rangein,
                "rin": rin,
                "primariesin": primariesin,
                "pin": pin,
                "transferin": transferin,
                "tin": tin,
                "matrixin": matrixin,
                "min": min,
                "chromal": chromal,
                "c": c,
                "chromalin": chromalin,
                "cin": cin,
                "npl": npl,
                "agamma": agamma,
                "param_a": param_a,
                "param_b": param_b,
            },
        )[0]
